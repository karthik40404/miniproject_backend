users = {}
events = {}
next_user_id = 1

while True:
    print("Welcome to Home Hero")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        if any(user["username"] == username for user in users.values()):
            print("Username already exists. Try a different one.")
        else:
            password = input("Enter password: ")
            phno=int(input("number please"))
            user_id = next_user_id
            next_user_id += 1
            users[user_id] = {"username": username, "password": password}
            print(f"Registration successful! Your user ID is {user_id}")

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        phno=int(input("number please"))
        user = next((user for user in users.values() if user["username"] == username and user["password"] == password), None)
        if user:
            user_id = next(key for key, value in users.items() if value["username"] == username)
            print(f"Login successful! Your user ID is {user_id}")
            # Event Management process
            while True:
                print("\nEvent Management")
                print("1. Add Event")
                print("2. View Events")
                print("3. Delete Event")
                print("4. Logout")
                event_choice = input("Enter your choice: ")

                if event_choice == '1':
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date: ")
                    if user_id not in events:
                        events[user_id] = {}
                    events[user_id][event_name] = event_date
                    print("Event added successfully!")

                elif event_choice == '2':
                    if user_id in events and events[user_id]:
                        print("Your Events:")
                        for event, date in events[user_id].items():
                            print(f"{event}: {date}")
                    else:
                        print("No events found.")

                elif event_choice == '3':
                    event_name = input("Enter event name to delete: ")
                    if user_id in events and event_name in events[user_id]:
                        del events[user_id][event_name]
                        print("Event deleted successfully!")
                    else:
                        print("Event not found.")

                elif event_choice == '4':
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid username or password.")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
