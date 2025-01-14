# Order Analysis Dashboard

## Overview
The Order Analysis Dashboard is a web application designed to help users find the optimal date to save orders in order to minimize refund amounts. It utilizes the Google Sheets API to fetch order and line item data, processes the information, and presents the results in a user-friendly interface.

## Features
- Input date range selection using a date picker.
- Analysis of orders to determine the best date to save.
- Displays the total refund amount associated with the best date.
- User-friendly error messages for invalid inputs.

## Prerequisites
Before running the application, ensure you have the following installed:
- Node.js (version 14 or higher)
- npm (Node Package Manager)
- A Google Cloud Project with the Google Sheets API enabled.
- A `credentials.json` file for Google Sheets Service in the root directory.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd order-analyzer
   ```

2. Install required dependencies:
   ```bash
   npm install
   ```

3. Set up your Google Cloud credentials:
   - Create a Google Cloud Project.
   - Enable the Google Sheets API.
   - Download the `credentials.json` file and place it in the root directory.

## Running the Application
1. Start the server:
   ```bash
   nodemon server.js
   ```
   The server will start running on port 3000. You should see the message "running on port 3000" in the console.

2. Access the application:
   Navigate to [http://localhost:3000](http://localhost:3000) in your web browser.

## Using the Application
1. In the web interface, select a Start date and an End date using the date picker.
2. Click the "Analyze Orders" button.
3. View results below the form, including the Best Date to save and the total refund amount.
4. Any errors will be displayed in red.

## Solution Approach
The application addresses the problem of finding the optimal date to save orders to minimize refund amounts through the following methods:
- **Data Structure Design**: Utilizes Map data structures for efficient lookups.
- **Algorithm Implementation**: Iterates through each date in the range to calculate total refund amounts.
- **Optimization Techniques**: Implements parallel fetching of spreadsheet data and efficient date parsing.
- **Error Handling**: Validates user input and handles errors gracefully.

## Testing
To test the application:
1. Create a test Google Spreadsheet with the following structure:

   **Orders Sheet:**
   | Order ID | Order Date  |
   |----------|-------------|
   | 1        | 01-01-2023  |
   | 2        | 02-01-2023  |
   | ...      | ...         |

   **LineItems Sheet:**
   | LineItem ID | Order ID | Price   |
   |-------------|----------|---------|
   | 101         | 1        | 100.50  |
   | 102         | 2        | 200.75  |
   | ...         | ...      | ...     |

2. Make the spreadsheet publicly accessible with view permissions.
3. Update the `spreadsheetId` in `server.js` with your spreadsheet ID.
4. Run test cases with different date ranges.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to [Google Cloud](https://cloud.google.com/) for providing the Sheets API.
- Special thanks to the contributors and the community for their support.