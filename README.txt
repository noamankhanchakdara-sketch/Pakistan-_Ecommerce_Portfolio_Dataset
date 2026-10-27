PAKISTAN E-COMMERCE PORTFOLIO DATASET
=====================================
Realistic SYNTHETIC practice data, not actual company data.

Files:
- customers.csv: customer profile, city/region, signup date, segment
- products.csv: product/category, unit cost, list price, supplier
- orders.csv: order date, customer, payment, status, shipping cost, delivery days
- order_items.csv: product line, quantity, unit price, discount, sales, product cost, gross profit

Relationships:
customers[Customer_ID] 1 -> * orders[Customer_ID]
orders[Order_ID] 1 -> * order_items[Order_ID]
products[Product_ID] 1 -> * order_items[Product_ID]

Definitions:
Sales = Quantity * Unit_Price - Discount_Amount
Product_Cost = Quantity * Unit_Cost
Gross_Profit = Sales - Product_Cost
Shipping_Cost is at order level. For contribution profit, subtract shipping once per order
or allocate it across line items; do not subtract it once per line without allocation.

Intentional data-quality issues:
- 8 customer records have missing City values.
- 5 duplicate line-item rows are included for duplicate detection.
- Cancelled, Returned, and Pending statuses require a documented reporting rule.
- Delivery_Days is blank for statuses other than Delivered or Returned.

Portfolio questions:
1. Total Sales, Gross Profit, and Gross Profit Margin?
2. Which categories/products have high sales but low margin?
3. Monthly sales/profit trend?
4. Which cities/regions contribute most to sales and profit?
5. How do discounts relate to profit margin?
6. Cancellation and return rates?
7. Which payment methods/customer segments perform best?
8. Are there duplicate lines, missing fields, or relationship integrity issues?

Suggested model:
Customers and Products as dimensions; Orders as order header; Order Items as sales line fact;
create a separate Calendar table related to Orders[Order_Date]. Document rules for statuses.
