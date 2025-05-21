monthly_income = int(input("Enter you monthly income"))
monthly_expenses = int (input("Enter your monthly expenses"))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings is: {monthly_savings}")
print(f"Your projected annual savings after interest is: {projected_annual_savings}")