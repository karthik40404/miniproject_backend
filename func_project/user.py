users = {}
admins = {'admin': 'admin123'}  # Example admin account
logged_in_users = {}

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

def logout(username):
    if username in logged_in_users:
        del logged_in_users[username]
        print("Logout successful.")
    else:
        print("User not logged in.")

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

def view_preferences(username):
    if username in users:
        preferences = users[username]['preferences']
        if preferences:
            print(f"Current preferences for {username}: {preferences}")
        else:
            print(f"No preferences set for {username}.")
    else:
        print("User not found.")

def delete_user(username):
    if username in users:
        del users[username]
        if username in logged_in_users:
            del logged_in_users[username]
        print("User account deleted.")
    else:
        print("User not found.")

def find_matches():
    matches = {}
    for user, data in users.items():
        matches[user] = []
        for other_user, other_data in users.items():
            if user != other_user:
                if all(other_data['profile'].get(key) == value for key, value in data['preferences'].items()):
                    matches[user].append(other_user)
    return matches
