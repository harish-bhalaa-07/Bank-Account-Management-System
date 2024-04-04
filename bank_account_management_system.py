def check_balance():
    global transaction_history
    balance = 0
    for transaction in transaction_history:
        if transaction[0] == 'deposit':
            balance += transaction[1]
        elif transaction[0] == 'withdrawal':
            balance -= transaction[1]
    return balance
    
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
