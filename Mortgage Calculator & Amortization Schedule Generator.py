import numpy_financial as npf #library for financial maths
import pandas as pd #library for working on tables of data
import matplotlib.pyplot as plt #part of library used for making charts and graphs

#take user imports
loan_amount = float(input("Enter the loan amaount: "))
annual_interest_rate = float(input("Enter annual interest rate in %: "))/100
loan_term_years = int(input("Enter the loan term in years: "))
payments_per_year = int(input("Enter number of payments per year (eg. 12 for monthly): "))

total_payments = loan_term_years*payments_per_year
periodic_rate = annual_interest_rate/payments_per_year

#monthly payment calculations
payment = npf.pmt(periodic_rate, total_payments, -loan_amount) #npf.pmt is a function from npf library that calculates the fixed payment per period/month
print(f"\nMonthly Payment: INR{payment:.2f}")

#generate amortization table
schedule = []
balance = loan_amount 

for i in range(1, total_payments+1):
    interest = balance*periodic_rate
    principal = payment - interest
    balance = balance - principal
    balance = max(balance,0) #avoid negative rounding error
    schedule.append([i,round(payment,2), round(principal,2), round(interest,2), round(balance,2)])

df = pd.DataFrame(schedule, columns=["Period","Payment","Principal","Interest","Balance"])
print("\nAmortization Table(First 5 Periods):") #shows a preview
print(df.head())

#Plotting principal vs interest
plt.figure(figsize=(10,10))
plt.plot(df["Period"], df["Principal"], label="Principal Paid", color='green')
plt.plot(df["Period"], df["Interest"], label="Interest Paid", color='red')
plt.title("Loan Amortization: Principal vs Interest")
plt.xlabel("Period")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




