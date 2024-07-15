from user import register_user, login, logout, set_preferences, edit_preferences, view_preferences, delete_user
from adm import admin_view

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            username, role = login()
            if username and role == 'user':
                while True:
                    print("\n1. Set Preferences\n2. Edit Preferences\n3. View Preferences\n4. Delete Account\n5. Logout\n6. Quit")
                    user_choice = input("Choose an option: ")
                    if user_choice == '1':
                        set_preferences(username)
                    elif user_choice == '2':
                        edit_preferences(username)
                    elif user_choice == '3':
                        view_preferences(username)
                    elif user_choice == '4':
                        delete_user(username)
                        break
                    elif user_choice == '5':
                        logout(username)
                        break
                    elif user_choice == '6':
                        break
                    else:
                        print("Invalid option. Try again.")
            elif username and role == 'admin':
                while True:
                    print("\n1. View Data\n2. Logout\n3. Quit")
                    admin_choice = input("Choose an option: ")
                    if admin_choice == '1':
                        admin_view()
                    elif admin_choice == '2':
                        logout(username)
                        break
                    elif admin_choice == '3':
                        return
                    else:
                        print("Invalid option. Try again.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
