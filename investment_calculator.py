import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

year = []
annual_income = []
annual_expenses = []
annual_investments = []
annual_returns = []
total_contributions = []

income = 145000
expenses = 45000
inflation = 0.02045 #average inflation over the last 10 years
interest_rate = 0.109 #average Annualized Return (Nominal) for the last 50 years
investment_principal = income - expenses #since investing the other half not used in expenses
adjusted_interest = interest_rate - inflation
contributions = income - expenses 
annual_return = investment_principal * interest_rate
current_year = 2021
added_contributions = 0

year.append(current_year)
annual_income.append(income)
annual_expenses.append(expenses)
annual_investments.append(investment_principal)
annual_returns.append(annual_return)
total_contributions.append(added_contributions)


investment_years = 20
for i in range(investment_years-1):
    investment_principal += annual_return + income / 2
    annual_return = investment_principal * adjusted_interest
    added_contributions += contributions

    year.append(current_year+i+1)
    annual_income.append(income)
    annual_expenses.append(expenses)
    annual_investments.append(investment_principal)
    annual_returns.append(annual_return)
    total_contributions.append(added_contributions)

df = pd.DataFrame()
df['Year'] = year
df['Annual Income'] = annual_income
df['Annual Expenses'] = annual_expenses
df['annual investments'] = annual_investments
df['annual returns'] = annual_returns
df['Contributions'] = total_contributions
print(df)

plt.figure(figsize=(15, 7))
plt.plot(df['Year'], df['annual investments'], label='Total Portfolio Amount')
plt.plot(df['Year'], df['Contributions'], label='Contributions')
plt.title("Balance Accumulation Graph")
plt.xlabel("Years")
plt.ylabel("$")
plt.xticks(df['Year'])
plt.legend()
plt.show()
