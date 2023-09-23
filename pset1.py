annual_salary = float(input("Enter your annual salary:​ "))

total_cost = 1000000

semi_annual_raise = float(0.07)

portion_down_payment = .25

current_saving = 0.0

r = 0.04

monthly_salary = annual_salary /12

month = 36


while(current_saving < (total_cost * portion_down_payment)):
    current_saving += current_saving *  (r / 12)
    current_saving += portion_saved * monthly_salary
    month += 1

    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary /12
    

print("Number of months:​ ", month)