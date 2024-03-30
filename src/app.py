import accounts
import chatbot
import chatdb
import physion

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    accounts.register(username, password)

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if accounts.login(username, password):
        print(f"Welcome, {username}!")
        return username
    else:
        print("Login failed.")
        return None

def main_menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def user_menu(username):
    print(f"[{username}] > ", end="")
    user_input = input()
    
    if user_input.lower() == "help":
        print("Help:")
        print("1. 'physion' - start cv bot")
        print("2. 'chat' - ask question to the chatbot")
        print("3. 'chatdb' - ask question about data stored in db")
        print("4. 'logout' - logout from your account")
    elif user_input.lower() == "physion":
        physion.physion_bot()
    elif user_input.lower() == "chat":
        chatbot.chat_with_gpt()
    elif user_input.lower() == "chatdb":
        chatdb.chat_with_db()

    return user_input.lower()


def main():
    logged_in_user = None
    actions = {'1': register_user, '2': login_user, '3': exit}
    try:
        while True:
            if logged_in_user:
                action = user_menu(logged_in_user)
                if action == 'logout':
                    logged_in_user = None
            else:
                choice = main_menu()
                action = actions.get(choice)
                if action:
                    result = action()
                    if result:
                        logged_in_user = result
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\nExiting the program.")

if __name__ == "__main__":
    main()
