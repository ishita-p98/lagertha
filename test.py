import json
import os
#file to store expense data
data_file = "expense.json"

#load data from file if it exists
def load_expenses():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return[] 

#save data to file
def save_expenses(expenses):
    with open(data_file, "w") as f:
        json.dump(expenses, f, indent=4)  

#add a new expense
def add_expense(expenses):
    date = input("Enter date(DD-MM-YYYY): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category(eg. food, transport, rent):")
    expense = {"date": date,"amount": amount,"category": category}
    expenses.append(expense)
    print("Expense Added!") 

#view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
    for e in expenses:
        print(f"{e['date']} - INR{e['amount']} on [{e['category']}]")

#summarize by category
def summarize_by_category(expenses):
    summary ={}
    for e in expenses:
        category = e["category"]
        summary[category] = summary.get(category,0)+e["amount"]
        
    print("\n---Expense Summary by Category---")
    for cat, total in summary.items():
        print(f"{cat}:INR{total:.2f}")

if __name__=="_main_":
    main()

