import numpy as np

sales = np.array(
    [
        [120, 150, 180, 200, 220, 250],  # Laptop
        [300, 280, 350, 400, 420, 450],  # Phone
        [100, 120, 110, 130, 140, 150],  # Headphones
        [200, 220, 250, 270, 300, 320],  # Monitor
        [80, 90, 100, 120, 130, 140],  # Keyboard
    ]
)
products = np.array(["Laptop", "Phone", "Headphones", "Monitor", "Keyboard"])

months = np.array(["January", "February", "March", "April", "May", "June"])
# df = pd.DataFrame(sales, columns=months, index=products)
total = np.sum(sales, axis=1)
averages = np.mean(sales, axis=1)
best_selling_product = np.argmax(total)
low_selling_product = np.argmin(total)
total_sale_per_month = np.sum(sales, axis=0)
best_sell_month = np.argmax(total_sale_per_month)
sales_above_1k = total > 1000
product_name_above_1k = products[sales_above_1k]
increased_sales = sales * 1.10
high_sale = sales[sales > 300]
print("""========== SALES REPORT ==========
""")
for product, total_sale, avg in zip(products, total, averages):
    print(f"{product}\n Total sales :{total_sale}\n Average sales :{avg:.2f}\n")
print("""====================
""")
print("Best Selling Product :", products[best_selling_product])
print(
    "Lowest Selling Product :",
    products[low_selling_product],
)
print("Best sales month :", months[best_sell_month])
print("\nProduct above 1k sales:")
for product_1k in product_name_above_1k:
    print(product_1k)
print("\n Increased sales :\n")
print(increased_sales)
print("\n Sales greater than 300 are:")
print(high_sale)
