
import numpy as np
# defining the constants
annual_salary = float(input("Enter your annual salary:"))
total_cost = 1000000
semi_annual_raise = 1.07
semi_annual = 1
number_of_months = 36

portion_down_payment = 0.25 * total_cost
r = 1 + (0.04 / 12)
i = 0
result = [0] * 36

# calculating the annual salary
for x in range(0, 36):
    i = i + 1
    result[x] = annual_salary * semi_annual
    if (i / 6) == 1:
        semi_annual = semi_annual_raise * semi_annual
        i = 0
annual_salary = result

# Bisection analyse
current_savings = [0] * 36
i = 36

for x in range(0, 36):
    current_savings[x] = (annual_salary[x] / 12) * (r**i)
    i = i - 1

portion_saved = portion_down_payment / sum(current_savings)
print("Best savings rate:" + str(portion_saved))
