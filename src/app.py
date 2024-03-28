import accounts

def main():
    try:
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                accounts.register(username, password)
                print("User registered successfully.")
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if accounts.login(username, password):
                    print(f"Welcome, {username}!")
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