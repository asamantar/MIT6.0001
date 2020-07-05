annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(
    input("Enter the precent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 1 + (0.04 / 12)
n = 0
i = 0


while current_savings < portion_down_payment:

    current_savings = (current_savings + (annual_salary / 12)
                       * portion_saved) * r
    n = n + 1
    i = i + 1
    if (i / 6) == 1:
        annual_salary = annual_salary * (semi_annual_raise + 1.0)
        i = 0


print("Number of months:" + str(n))
