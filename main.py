import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
order_items = pd.read_csv('order_items.csv')

merged = orders.merge(customers, on='Customer_ID', how='left')
full_data = merged.merge(order_items, on='Order_ID', how='left')

total_sales = order_items['Sales'].sum()
total_profit = order_items['Gross_Profit'].sum()
print(f"Total Sales: Rs. {total_sales:,.0f}")
print(f"Total Profit: Rs. {total_profit:,.0f}")

city_sales = full_data.groupby('City')['Sales'].sum().sort_values(ascending=False)
print("\nTop 10 Cities:")
print(city_sales.head(10))

plt.figure(figsize=(10,6))
city_sales.head(10).plot(kind='bar', color='#0a9396')
plt.title('Top 10 Cities by Sales - Pakistan E-Commerce')
plt.ylabel('Sales (Rs.)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('city_sales_graph.png')
print("\n✅ Graph Saved")

payment = full_data.groupby('Payment_Method')['Sales'].sum().sort_values(ascending=False)
print("\nPayment Method Sales (Proper Rs.):")
for method, amount in payment.items():
    print(f"{method}: Rs. {amount:,.0f}")
    # Monthly Sales Trend
full_data['Order_Date'] = pd.to_datetime(full_data['Order_Date'], errors='coerce')
monthly_sales = full_data.groupby(full_data['Order_Date'].dt.strftime('%Y-%m'))['Sales'].sum().sort_index()

plt.figure(figsize=(12,5))
monthly_sales.plot(color='#e63946', marker='o')
plt.title('Monthly Sales Trend - Pakistan E-Commerce')
plt.ylabel('Sales (Rs.)')
plt.xlabel('Month')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monthly_sales_graph.png')
print("✅ Monthly Graph Saved: monthly_sales_graph.png")
oct_data = full_data[full_data['Order_Date'].dt.strftime('%Y-%m') == '2024-10']
print(oct_data['Category'].value_counts())