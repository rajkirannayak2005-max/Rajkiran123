# Initial balance
balance = 1000

# Function to check balance
def check_balance():
    print("Your current balance is:", balance)

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")
    print("Updated balance is:", balance)

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance is:", balance)
    else:
        print("Insufficient balance!")

# Main loop
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid choice! Please try again.")
