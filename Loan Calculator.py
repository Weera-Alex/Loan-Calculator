import math

type = input("""What do you want to calculate? 
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if type == "n":
    principal = int(input("Enter the loan principal:\n"))
    monthly = int(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest * 0.001 / (12 * 0.10)
    n = math.ceil(math.log(monthly / (monthly-i * principal), 1 + i))
    year = math.floor(n / 12)
    month = n % 12
    if year == 0:
        print(f"It will take {month} month{'s' if month > 1 else ''} to repay the loan")
    elif month == 0:
        print(f"It will take {year} year{'s' if year > 1 else ''} to repay the loan")
    else:
        print(f"It will take {year} year{'s' if year > 1 else ''} and {month} month{'s' if month > 1 else ''} to repay this loan!")

elif type == "a":
    principal = int(input("Enter the loan principal:\n"))
    period = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest * 0.001 / (12 * 0.10)
    calc = math.ceil(principal * (i * (1 + i)**period) / ((1 + i)**period - 1))
    print(f"Your monthly payment = {calc}!")

elif type == "p":
    annuity = float(input("Enter the annuity payment:\n"))
    period = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest * 0.001 / (12 * 0.10)
    P = annuity / ((i * (1 + i)**period) / ((1 + i)**period -1))
    print(f"Your loan principal = {int(P)}!")