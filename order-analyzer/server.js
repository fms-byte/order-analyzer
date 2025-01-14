const express = require("express");
const { google } = require("googleapis");
const path = require("path");
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

// Helper function to Parse Date from dd-mm-yyyy to Date(yyyy-mm-dd)
function parseDate(dateStr) {
    const [day, month, year] = dateStr.split("-");
    return new Date(year, month - 1, day);
}

// Helper function to Parse dateString(dd-mm-yyyy) from Date format (yyyy-mm-dd)
function formatDate(date) {
    const day = String(date.getDate()).padStart(2, "0");
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const year = date.getFullYear();
    return `${day}-${month}-${year}`;
}

async function findBestDay(orders, lineItems, startDate, endDate) {
    // Remove headers
    const orderData = orders.values.slice(1);
    const lineItemData = lineItems.values.slice(1);

    // Create a map of order dates and their associated line items
    const orderMap = new Map();
    orderData.forEach(([orderId, dateStr]) => {
        orderMap.set(orderId, dateStr);
    });

    // Create a map of dates and their total prices
    const dateMap = new Map();
    lineItemData.forEach(([lineItemId, orderId, price]) => {
        const dateStr = orderMap.get(orderId);
        if (!dateMap.has(dateStr)) {
            dateMap.set(dateStr, 0);
        }
        dateMap.set(dateStr, dateMap.get(dateStr) + Number(price));
    });

    // Parse date range
    const start = parseDate(startDate);
    const end = parseDate(endDate);
    let bestDate = null;
    let minTotalRefund = Infinity;

    // For each possible date to save
    for (
        let date = new Date(start);
        date <= end;
        date.setDate(date.getDate() + 1)
    ) {
        const dateStr = formatDate(date);
        let totalRefund = 0;

        // Calculate total refund if we save this date
        for (const [orderDate, total] of dateMap) {
            if (
                orderDate !== dateStr &&
                parseDate(orderDate) >= start &&
                parseDate(orderDate) <= end
            ) {
                totalRefund += total;
            }
        }

        // Update best date if this results in lower total refund
        if (totalRefund < minTotalRefund) {
            minTotalRefund = totalRefund;
            bestDate = dateStr;
        }
    }

    return {
        bestDate,
        totalRefundAmount: minTotalRefund,
    };
}

// Serve index.html file at root
app.get("/", async (req, res) => {
    const { startDate, endDate } = req.query;

    // If there are no query parameters, serve the HTML file (requires Start Date and End Date)
    if (!startDate || !endDate) {
        return res.sendFile(path.join(__dirname, "index.html"));
    }

    // Otherwise, process the analysis request
    try {
        // Validate date format
        const dateRegex = /^\d{2}-\d{2}-\d{4}$/;
        if (!dateRegex.test(startDate) || !dateRegex.test(endDate)) {
            return res.status(400).json({
                error: "Invalid date format. Use dd-mm-yyyy",
            });
        }

        const auth = new google.auth.GoogleAuth({
            keyFile: "./credentials.json",
            scopes: "https://www.googleapis.com/auth/spreadsheets",
        });

        const client = await auth.getClient();
        const sheets = google.sheets({ version: "v4", auth: client });
        const { spreadsheetId } = require("./parameters.json");

        // Fetch both sheets in parallel
        const [ordersResponse, lineItemsResponse] = await Promise.all([
            sheets.spreadsheets.values.get({
                auth,
                spreadsheetId,
                range: "Orders!A:B",
            }),
            sheets.spreadsheets.values.get({
                auth,
                spreadsheetId,
                range: "LineItems!A:C",
            }),
        ]);

        // Find the best day
        const result = await findBestDay(
            ordersResponse.data,
            lineItemsResponse.data,
            startDate,
            endDate
        );

        res.json({
            status: "success",
            ...result,
        });
    } catch (error) {
        console.error("Error:", error);
        res.status(error.status).json({
            // error: "Internal server error",
            message: error.message,
        });
    }
});

app.listen(3000, () => console.log("running on port 3000"));
