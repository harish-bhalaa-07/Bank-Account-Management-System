def deposit_money(amount):
    global transaction_history
    transaction_history.append(('deposit', amount))
    print(f"Deposited ${amount} into your account.")

def bank_account_management():
    while True:
        print("\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. View Transaction History\n5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit_money(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(amount)
        elif choice == '3':
            balance = check_balance()
            print(f"Current Balance: ${balance}")
        elif choice == '4':
            view_transaction_history()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

bank_account_management()
