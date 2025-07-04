import pandas as pd #used for creating and managing structured data
import matplotlib.pyplot as plt #used for plotting graphs
import seaborn as sns #high-level interface for drawing statistical graphics

#define weights of each factor based on FICO model
credit_weights = {
    "Payment History": 0.35, #how reliabaly paid past loans
    "Credit Utilization": 0.30, #how much available credit is being used
    "Credit History Length": 0.15, #how long credit accounts have been held
    "New Credit Inquiries": 0.10, #how often credit has been applied for recently
    "Credit Mix": 0.10, #variety in types of credit accounts (eg. loans, card)
}

#for user input (in real life this is accessed directly from lenders, institutions etc)
def get_user_input():
    print("Please provide the following financial behavior metrics (0–100 scale):")
    try:
        payment_history = float(input("% On-time Payment History score(e.g., 98): "))
        credit_utilization = float(input("% Credit Utilization score(e.g., 25): "))
        credit_history_length = float(input("Credit History Score (e.g., 85): "))
        new_credit_inquiries = float(input("New Credit Inquiries Score (e.g., 10): "))
        credit_mix = float(input("Credit Mix Score (e.g., 80): "))
    except ValueError:
        print("Invalid input.Please enter numbers only")
        return None
    
    return{
        "Payment History": payment_history,
        "Credit Utilization": credit_utilization,
        "Credit History Length": credit_history_length,
        "New Credit Inquiries": new_credit_inquiries,
        "Credit Mix": credit_mix
    }

#to normalize and calculate weighted score
def calculate_credit_score(inputs):
    score = 0
    for factor, weight in credit_weights.items():
        if factor == "Credit Utilization":
            normalized = 100 - inputs[factor] #lower utilization is better
        elif factor == "New Credit Inquiries":
            normalized = 100 - inputs[factor] #fewer inquiries is better
        else:
            normalized = inputs[factor] #higher is better
        score += normalized*weight
    return int(300+(score/100)*550) #Scale score is between 300-850

#generate radar chart
def plot_radar(data):
    labels = list(data.keys())
    values = list(data.values())
    values += values[:1]
    labels += labels[:1]

    angles = [n/float(len(/labels))*2*3.14159 for n in range(len(lables))]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2) #outline shape
    ax.fill(angles, values, alpha=0.25) #soft fill inside the shape
    ax.set_yticklabels([]) #hides the circular grid labels
    ax.set_xticks(angles) #places text at correct angle points
    ax.set_xticklabels(labels) #adds the labels like "Credit Mix"
    ax.title("Credit Score Factor Breakdown")
    plt.show

#visualize current vs simulated score via bar graph
def plot_score_comparison(current, simulated):
    df = pd.DataFrame({
        "Type": ["Current", "Simulated"],
        "Credit Score": [current,simulated]
    })
    sns.barplot(data=df, x="Type", y="Credit Score", palette="viridis")
    plt.title("Credit Score Comparison")
    plt.ylim(300, 850)
    plt.show()

#run program
user_input = get_user_input()

if user_input:
    current_score = calculate_credit_score(user_input)
    print(f"\nYour current simulated credit score is: {current_score}")

    simulated_input = user_input.copy()
    simulated_input["Payment History"] = 100
    simulated_input["Credit Utilization"] = 10
    simulated_score = calculate_credit_score(simulated_input)
    print(f"With improved behavior, your score could become: {simulated_score}\n")

    plot_radar(user_input)
    plot_score_comparison(current_score, simulated_score)
else:
    print("Invalid input!")


