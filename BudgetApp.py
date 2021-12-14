# A Budget app
# It instantiate objects based on different budget categories
# like food,clothing and entertainment
# Depositing funds to each of the categories
# withdrawing funds from each category
# Computing category balance
# Transferring balance amount between categories

# We begin
import time
import BudgetStimulator
# We start.... pewwww


def budget_app():
    ad1()
    repeat = "Yes"
    while repeat == "Yes":
        category = input("Enter your preferred category: ").capitalize()
        print("\n")
        if category == "Food":
                food()

        elif category == "Clothing":
                clothing()

        elif category == "Entertainment":
                entertainment()

        elif category == "Others":
                other()

        repeat = input("Like To perform more operation, Enter Yes or No, To Halt Operation: ").capitalize()


def ad1():
    print("Welcome to Budget App")
    time.sleep(2)
    print("We have you covered on whatever category you might want to have your budget")
    time.sleep(1)
    print("We have categories like:\n\tFood\n\tClothing\n\tEntertainments(subscription,etc....)\n\tOthers")
    print("It's Quite easy to use")


def ad2():
    print("\tTo Deposit, Enter D\n\tTo Withdraw, Enter W\n\tTo Transfer, Enter T....")


def food():
    new_bal = 0.0
    repeat01 = "Yes"
    print("Welcome to Food Category....")
    while repeat01 == "Yes":
        time.sleep(2)
        print("Make simple Food Budget\nThere are varieties of operation you can do here. ")
        ad2()
        bal = 0.0
        prompt = input("Your choice: ").capitalize()

        if prompt == "D":
            new_bal = ultra_deposit(bal)
        bal =+ new_bal

        if prompt == "W":
                if new_bal == 0:
                    print("Insufficient funds...")
                    print("\n")
                elif new_bal > 0:
                    print("\n")
                    cash =- ultra_withdrawal(new_bal)
                    print("\n")

        elif prompt == "T":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash = - ultra_transfer(new_bal)
                print("\n")

        repeat01 = input("like to continue in this Category: ").capitalize()


def clothing():
    new_bal = 0.0
    repeat02 = "Yes"
    print("Welcome to Clothing Category....")
    while repeat01 == "Yes":
        time.sleep(2)
        print("Make simple Clothing Budget\nThere are varieties of operation you can do here. ")
        ad2()
        bal = 0.0
        prompt = input("Your choice: ").capitalize()

        if prompt == "D":
            new_bal = ultra_deposit(bal)
        bal = + new_bal

        if prompt == "W":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash = - ultra_withdrawal(new_bal)
                print("\n")

        elif prompt == "T":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash = - ultra_transfer(new_bal)
                print("\n")

        repeat02 = input("like to continue in this Category: ").capitalize()


def entertainment():
    new_bal = 0.0
    repeat01 = "Yes"
    print("Welcome to Food Category....")
    while repeat01 == "Yes":
        time.sleep(2)
        print("Make simple Food Budget\nThere are varieties of operation you can do here. ")
        ad2()
        bal = 0.0
        prompt = input("Your choice: ").capitalize()

        if prompt == "D":
            new_bal = ultra_deposit(bal)
        bal = + new_bal

        if prompt == "W":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash = - ultra_withdrawal(new_bal)
                print("\n")

        elif prompt == "T":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash = - ultra_transfer(new_bal)
                print("\n")

        repeat01 = input("like to continue in this Category: ").capitalize()


def other():
    new_bal = 0.0
    repeat01 = "Yes"
    print("Welcome to Others Category....")
    while repeat01 == "Yes":
        time.sleep(2)
        print("Make simple Budget for whatever you have in mind to budget"
              "\nThere are varieties of operation you can do here. ")
        ad2()
        bal = 0.0
        prompt = input("Your choice: ").capitalize()

        if prompt == "D":
            new_bal = ultra_deposit(bal)
        bal =+ new_bal

        if prompt == "W":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash =- ultra_withdrawal(new_bal)
                print("\n")

        elif prompt == "T":
            if new_bal == 0:
                print("Insufficient funds...")
                print("\n")
            elif new_bal > 0:
                print("\n")
                cash =- ultra_transfer(new_bal)
                print("\n")

        repeat01 = input("like to continue in this Category: ").capitalize()


def ultra_deposit(bal):
    funds = 0.0
    budget = BudgetStimulator.BudgetWork(bal)
    amount = float(input("How much are you funding this week: "))
    budget.deposit(amount)
    print(f"\t{amount} has been added to the Category..")
    time.sleep(3)
    print("You now have #", format(budget.get_balance(), ".2f"), sep=" ")
    funds += budget.get_balance()

    return funds


def ultra_withdrawal(funds):
    budget = BudgetStimulator.BudgetWork(funds)
    amount = float(input("Enter funds for the week Budget: "))
    if funds > amount:
        budget.withdraw(amount)
        print(f"You are withdrawing {amount} for this week upkeep...")
        time.sleep(4)
        print("Done withdrawing")
        time.sleep(3)
        print("Your Budget is #", format(budget.get_balance(), ".2f"), sep=" ")
    else:
        print("Insufficient Balance.....")

    funds = budget.get_balance()

    return funds


def ultra_transfer(bal):
    budget = BudgetStimulator.BudgetWork(funds)
    amount = float(input("Enter funds for the week Budget: "))
    if funds > amount:
        budget.withdraw(amount)
        print(f"You are withdrawing {amount} for this week upkeep...")
        time.sleep(4)
        print("Done withdrawing")
        time.sleep(3)
        print("Your Budget is #", format(budget.get_balance(), ".2f"), sep=" ")
    else:
        print("Insufficient Balance.....")

    funds = budget.get_balance()

    return funds


budget_app()