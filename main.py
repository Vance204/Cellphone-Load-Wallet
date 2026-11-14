
from load_wallet import LoadWallet


def main():

    owner = input("Enter owner name: ").strip()
    number = input("Enter mobile number: ").strip()

    if not owner or len(number) != 11 or not number.startswith("09") or not number.isdigit():
        print("Invalid owner name or mobile number.")
        return

    try:
        starting_balance = int(input("Enter starting balance: P"))

        if starting_balance < 0:
            print("Starting balance cannot be negative.")
            return

    except ValueError:
        print("Invalid starting balance.")
        return

    wallet = LoadWallet(owner, number, starting_balance)

    print("""\n----- MENU -----
1. Top Up Load
2. Send Load (same network)
3. Send Load (other network, with fee)
4. Show Balance
5. Exit""")

    while True:


        try:
            choice = int(input("\nChoose an option (1-5): "))

            if choice == 1:
                amount = int(input("Enter top-up amount: P"))
                wallet.top_up(amount)

            elif choice == 2:
                recipient = input("Enter recipient number: ")
                amount = int(input("Enter amount to send: P"))
                wallet.send_load(recipient, amount)

            elif choice == 3:
                recipient = input("Enter recipient number: ")
                amount = int(input("Enter amount to send: P"))
                fee = int(input("Enter service fee: P"))
                wallet.send_with_fee(recipient, amount, fee)

            elif choice == 4:
                wallet.show_balance()

            elif choice == 5:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Enter 1-5.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
