annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(
    input("Enter the precent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 1 + (0.04 / 12)
r = 0
n = 0

while current_savings < portion_down_payment:
    current_savings = current_savings * r
    current_savings = current_savings + (annual_salary / 12) * portion_saved
    n = n + 1

print("Number of months:" + str(n))
