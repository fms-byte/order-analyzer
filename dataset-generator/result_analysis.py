import pandas as pd

# Load the CSV files
line_items_path = './data/line_items.csv'
orders_path = './data/orders.csv'

line_items = pd.read_csv(line_items_path)
orders = pd.read_csv(orders_path)

# Merge line_items with orders to get order dates
merged_data = pd.merge(line_items, orders, on="Order ID")

# Export the marged data into a new csv
merged_data.to_csv('./data/merged_data.csv', index=False)

# Convert date to datetime format with the correct format specified
merged_data['Order Date'] = pd.to_datetime(merged_data['Order Date'], format='%d-%m-%Y')

# Aggregate data by date
aggregated_data = merged_data.groupby('Order Date').agg(
    order_count=('Order ID', 'nunique'),
    total_amount=('Price', 'sum'),
    average_order_value=('Price', 'mean')
).reset_index()

# Find the highest and lowest order counts and amounts
highest_order_count = aggregated_data.loc[aggregated_data['order_count'].idxmax()]
lowest_order_count = aggregated_data.loc[aggregated_data['order_count'].idxmin()]

highest_total_amount = aggregated_data.loc[aggregated_data['total_amount'].idxmax()]
lowest_total_amount = aggregated_data.loc[aggregated_data['total_amount'].idxmin()]

# Find dates with maximum and minimum average order values
max_avg_order_value = aggregated_data.loc[aggregated_data['average_order_value'].idxmax()]
min_avg_order_value = aggregated_data.loc[aggregated_data['average_order_value'].idxmin()]

# Write results to a text file
result_path = './result.txt'
with open(result_path, 'w') as file:
    file.write("Survey Analysis Results\n")
    file.write("=======================\n\n")
    file.write(f"Highest Orders by Count:\nDate: {highest_order_count['Order Date'].strftime('%d-%m-%Y')}\nCount: {highest_order_count['order_count']}\n\n")
    file.write(f"Highest Orders by Amount:\nDate: {highest_total_amount['Order Date'].strftime('%d-%m-%Y')}\nAmount: {highest_total_amount['total_amount']:.2f}\n\n")
    file.write(f"Lowest Orders by Count:\nDate: {lowest_order_count['Order Date'].strftime('%d-%m-%Y')}\nCount: {lowest_order_count['order_count']}\n\n")
    file.write(f"Lowest Orders by Amount:\nDate: {lowest_total_amount['Order Date'].strftime('%d-%m-%Y')}\nAmount: {lowest_total_amount['total_amount']:.2f}\n\n")
    file.write(f"Maximum Average Order Value:\nDate: {max_avg_order_value['Order Date'].strftime('%d-%m-%Y')}\nAverage Value: {max_avg_order_value['average_order_value']:.2f}\n\n")
    file.write(f"Minimum Average Order Value:\nDate: {min_avg_order_value['Order Date'].strftime('%d-%m-%Y')}\nAverage Value: {min_avg_order_value['average_order_value']:.2f}\n\n")

print(f"Analysis complete. Results are saved in {result_path}.")
