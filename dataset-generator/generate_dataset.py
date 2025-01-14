import csv
import random
from datetime import datetime, timedelta

def generate_orders(start_date_str, end_date_str, num_orders):
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%Y')
    
    # Generate orders
    orders = []
    for order_id in range(1, num_orders + 1):
        # Random date between start and end date
        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)
        order_date = start_date + timedelta(days=random_days)
        
        orders.append({
            'Order ID': order_id,
            'Order Date': order_date.strftime('%d-%m-%Y')
        })
    
    # Sort orders by date
    orders.sort(key=lambda x: datetime.strptime(x['Order Date'], '%d-%m-%Y'))
    
    return orders

def generate_line_items(orders, items_per_order_range=(1, 3), price_range=(50, 500)):
    line_items = []
    line_item_id = 1
    
    for order in orders:
        # Random number of items for this order
        num_items = random.randint(items_per_order_range[0], items_per_order_range[1])
        
        for _ in range(num_items):
            price = round(random.uniform(price_range[0], price_range[1]), 2)
            line_items.append({
                'LineItem ID': line_item_id,
                'Order ID': order['Order ID'],
                'Price': price
            })
            line_item_id += 1
    
    return line_items

# Generate the data
orders = generate_orders('01-01-2023', '31-12-2023', 10000)  # Generate 10000 orders for 2023
line_items = generate_line_items(orders)

# Write Orders to CSV
with open('./data/orders.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Order ID', 'Order Date'])
    writer.writeheader()
    writer.writerows(orders)

# Write Line Items to CSV
with open('./data/line_items.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['LineItem ID', 'Order ID', 'Price'])
    writer.writeheader()
    writer.writerows(line_items)

print(f"Generated {len(orders)} orders and {len(line_items)} line items.")

