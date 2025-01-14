# Project Suite: Order Analysis and Dataset Generation

## Overview
This repository contains two related projects: **Order Analyzer** and **Dataset Generator**. The Order Analyzer is a web application with Express and NodeJS Server that helps users find the optimal date to save orders to minimize refund amounts, while the Dataset Generator is a tool designed to create sample datasets for testing and analysis purposes.

## Projects

### 1. Order Analyzer
The Order Analyzer is a web application that utilizes the Google Sheets API to fetch order and line item data, processes the information, and presents the results in a user-friendly interface.

#### Features
- Input date range selection using a date picker.
- Analysis of orders to determine the best date to save.
- Displays the total refund amount associated with the best date.
- User-friendly error messages for invalid inputs.

#### Installation and Usage: Read the [order-analyzer/README.md](./order-analyzer/README.md) file for detail instructions.

### 2. Dataset Generator
The Dataset Generator is a utility designed to create sample datasets for testing purposes. It can generate random order and line item data, which can be used to simulate various scenarios in the Order Analyzer.

#### Features
- Generate random datasets for orders and line items.
- Customizable parameters for dataset size and content.
- Easy integration with the Order Analyzer for testing.

#### Installation and Usage: Read the [dataset-generator/README.md](./dataset-generator/README.md) file for detail instructions.

## Testing
Both projects can be tested using sample datasets. For the Order Analyzer, create a Google Spreadsheet with the appropriate structure as described in the Order Analyzer's README. For the Dataset Generator, run the script to create datasets that can be imported into the Order Analyzer.
