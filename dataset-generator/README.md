# Dataset Generator and Order Analysis

## Overview
This project consists of two main scripts: `generate_dataset.py` and `result_analysis.py`. The purpose of these scripts is to generate a synthetic dataset of orders and line items, and then analyze the generated data to extract meaningful insights.

## Scripts

### 1. generate_dataset.py
This script is responsible for generating a synthetic dataset of orders and line items. It performs the following tasks:

- **Generate Orders**: 
  - Creates a specified number of orders (default is 10,000) with random order dates between a given start and end date (default is from 01-01-2023 to 31-12-2023).
  - Each order is assigned a unique Order ID and an Order Date.

- **Generate Line Items**: 
  - For each order, a random number of line items (between 1 and 3) is generated.
  - Each line item is assigned a unique Line Item ID and a random price within a specified range (default is between 50 and 500).

- **Output**: 
  - The generated orders are saved to `data/orders.csv`.
  - The generated line items are saved to `data/line_items.csv`.

### 2. result_analysis.py
This script analyzes the generated dataset to provide insights into the orders and line items. It performs the following tasks:

- **Load Data**: 
  - Reads the generated CSV files (`line_items.csv` and `orders.csv`) into pandas DataFrames.

- **Merge Data**: 
  - Merges the line items with the orders to include order dates in the analysis.

- **Data Aggregation**: 
  - Aggregates the data by order date to calculate:
    - Total number of unique orders per date.
    - Total amount of sales per date.
    - Average order value per date.

- **Insights Extraction**: 
  - Identifies the highest and lowest order counts and amounts.
  - Finds the dates with maximum and minimum average order values.

- **Output**: 
  - The analysis results are saved to `result.txt`, which includes a summary of the findings.

## Data Files
- `data/orders.csv`: Contains the generated orders with Order IDs and Order Dates.
- `data/line_items.csv`: Contains the generated line items with Line Item IDs, Order IDs, and Prices.
- `data/merged_data.csv`: Contains the merged data of orders and line items for analysis.
- `result.txt`: Contains the results of the analysis, including insights on order counts and values.

## Usage
1. Run `generate_dataset.py` to generate the dataset.
2. Run `result_analysis.py` to analyze the generated data and produce insights.
3. Check `result.txt` for the analysis results.

## Requirements
- Python 3.x
- pandas library (install via pip: `pip install pandas`)

## Conclusion
This project provides a simple way to generate synthetic order data and analyze it for insights, which can be useful for testing and demonstration purposes.

