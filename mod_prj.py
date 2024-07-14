# In-memory storage for users and admins
users = {}
admins = {'admin': 'admin123'}  # Example admin account
logged_in_users = {}

# Function to register a new user
def register_user():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    height = input("Enter height: ")
    hair_color = input("Enter hair color: ")
    age = int(input("Enter age: "))
    profile = {'height': height, 'hair_color': hair_color, 'age': age}
    users[username] = {'password': password, 'profile': profile, 'preferences': {}}
    print("User registered successfully.")

# Function for login (both user and admin)
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        logged_in_users[username] = 'user'
        print("User login successful.")
        return username, 'user'
    elif username in admins and admins[username] == password:
        logged_in_users[username] = 'admin'
        print("Admin login successful.")
        return username, 'admin'
    print("Invalid username or password.")
    return None, None

# Function for logout
def logout(username):
    if username in logged_in_users:
        del logged_in_users[username]
        print("Logout successful.")
    else:
        print("User not logged in.")

# Function to set user preferences
def set_preferences(username):
    if username in users:
        height = input("Enter preferred height: ")
        hair_color = input("Enter preferred hair color: ")
        age = int(input("Enter preferred age: "))
        preferences = {'height': height, 'hair_color': hair_color, 'age': age}
        users[username]['preferences'] = preferences
        print("Preferences updated.")
    else:
        print("User not found.")

# Function to edit user preferences
def edit_preferences(username):
    if username in users:
        height = input("Enter new preferred height: ")
        hair_color = input("Enter new preferred hair color: ")
        age = int(input("Enter new preferred age: "))
        preferences = {'height': height, 'hair_color': hair_color, 'age': age}
        users[username]['preferences'].update(preferences)
        print("Preferences edited successfully.")
    else:
        print("User not found.")

# Function to view user preferences
def view_preferences(username):
    if username in users:
        preferences = users[username]['preferences']
        if preferences:
            print(f"Current preferences for {username}: {preferences}")
        else:
            print(f"No preferences set for {username}.")
    else:
        print("User not found.")

# Function to delete a user account
def delete_user(username):
    if username in users:
        del users[username]
        if username in logged_in_users:
            del logged_in_users[username]
        print("User account deleted.")
    else:
        print("User not found.")

# Function to find matches
def find_matches():
    matches = {}
    for user, data in users.items():
        matches[user] = []
        for other_user, other_data in users.items():
            if user != other_user:
                if all(other_data['profile'].get(key) == value for key, value in data['preferences'].items()):
                    matches[user].append(other_user)
    return matches

# Function for admin to view all data
def admin_view():
    print("Admin View:")
    print("User Profiles:")
    for user, data in users.items():
        print(f"{user}: {data['profile']}")
    print("\nUser Preferences:")
    for user, data in users.items():
        print(f"{user}: {data['preferences']}")
    print("\nMatches:")
    matches = find_matches()
    for user, match_list in matches.items():
        print(f"{user} matches with: {', '.join(match_list) if match_list else 'No matches found'}")

# Main function to drive the application
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
