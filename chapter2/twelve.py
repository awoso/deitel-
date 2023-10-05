original_amount = int(input("Enter principal amount: "))
annual_return = float(input("Input rate: "))
number_of_years = int(input("Enter number of years: "))

prncipal = 1000
rate = 7/100

amount_after_10_years = prncipal * (1 + rate)**10

amount_after_10_years = (round(amount_after_10_years, 2))

print("$", amount_after_10_years)
