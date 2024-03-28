import accounts

def main():
    logged_in_user = None
    try:
        while True:
            if logged_in_user:
                while True:
                    print(f"[{logged_in_user}] > ", end="")
                    user_input = input()
                    if user_input.lower() == 'logout':
                        logged_in_user = None
                        break
                    else:
                        print(f"You entered: {user_input}")
            else:
                print("1. Register")
                print("2. Login")
                print("3. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    accounts.register(username, password)
                elif choice == '2':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if accounts.login(username, password):
                        print(f"Welcome, {username}!")
                        logged_in_user = username
                    else:
                        print("Login failed.")
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\nExiting the program.")

if __name__ == "__main__":
    main()