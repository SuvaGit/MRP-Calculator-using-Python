# Get input from user
cost_price = float(input("Enter cost price: "))

# Calculate MRP
profit_percent = float(input("Enter profit percent: "))
mrp = cost_price + (cost_price * profit_percent / 100)

# Display result
print("MRP: ", round(mrp, 2))