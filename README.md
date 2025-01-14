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

#### Installation and Usage
1. **Prerequisites**:
   - Node.js (version 14 or higher)
   - npm (Node Package Manager)
   - A Google Cloud Project with the Google Sheets API enabled.
   - A `credentials.json` file for Google Sheets Service in the root directory.

2. **Installation**:
   - Clone the repository:
     ```bash
     git clone <repository-url>
     cd order-analyzer
     ```
   - Install required dependencies:
     ```bash
     npm install
     ```

3. **Running the Application**:
   - Start the server:
     ```bash
     nodemon server.js
     ```
   - Access the application at [http://localhost:3000](http://localhost:3000).

4. **Using the Application**:
   - Select a Start date and an End date using the date picker.
   - Click the "Analyze Orders" button to view results.

### 2. Dataset Generator
The Dataset Generator is a utility designed to create sample datasets for testing purposes. It can generate random order and line item data, which can be used to simulate various scenarios in the Order Analyzer.

#### Features
- Generate random datasets for orders and line items.
- Customizable parameters for dataset size and content.
- Easy integration with the Order Analyzer for testing.

#### Installation and Usage
1. **Prerequisites**:
   - Python (version 3.6 or higher)
   - pandas library

2. **Installation**:
   - Clone the repository:
     ```bash
     git clone <repository-url>
     cd dataset-generator
     ```
   - Install required dependencies:
     ```bash
     pip install pandas
     ```

3. **Running the Dataset Generator**:
   - Execute the script to generate datasets for 10000 rows:
     ```bash
     python generate_dataset.py
     ```
   - The generated datasets will be saved in the ```.csv``` format in the ```dataset-generate/data``` directory.

4. **Running the Result Analysis Script**:
   - Execute the script to generate datasets for 10000 rows:
     ```bash
     python result_analysis.py
     ```
   - An analysis on the generated csv file will be generated on ```result.txt``` file in the same directory.

## Testing
Both projects can be tested using sample datasets. For the Order Analyzer, create a Google Spreadsheet with the appropriate structure as described in the Order Analyzer's README. For the Dataset Generator, run the script to create datasets that can be imported into the Order Analyzer.

## License
This project suite is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to [Google Cloud](https://cloud.google.com/) for providing the Sheets API.
- Special thanks to the contributors and the community for their support.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.