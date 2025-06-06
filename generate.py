import pandas as pd
import random
from datetime import datetime, timedelta

# Define sample products
products = ['Laptop', 'Phone', 'Headphones', 'Monitor', 'Keyboard', 'Mouse', 'Printer']

# Generate 100 synthetic transactions
data = []
for i in range(100):
    transaction_id = f"T{i+1:04d}"
    customer_id = f"C{random.randint(1000, 9999)}"
    product = random.choice(products)
    price = round(random.uniform(50, 1500), 2)
    quantity = random.randint(1, 5)

    # Generate transaction date within the last 10 days
    days_ago = random.randint(0, 10)
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
    transaction_date = datetime.now() - timedelta(days=days_ago) + random_time
    transaction_date = transaction_date.strftime('%Y-%m-%d %H:%M:%S')

    data.append([transaction_id, customer_id, product, price, quantity, transaction_date])

# Create DataFrame and save
df = pd.DataFrame(data, columns=['transaction_id', 'customer_id', 'product', 'price', 'quantity', 'transaction_date'])
df.to_csv('custom_data.csv', index=False)

print("Dataset saved as custom_data.csv with", len(df), "rows.")

