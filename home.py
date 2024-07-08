from datetime import datetime

# Define dictionaries to store user and service provider information
users = {}

service_providers = {
    'plumber': [
        {'name': 'John', 'location': '101 Maple St', 'work_locations': ['a']}
    ],
    'electrician': [
        {'name': 'Alex', 'location': '303 Cedar St', 'work_locations': ['a']}
    ],
    'maid': [
        {'name': 'Anna', 'location': '123 Pine St', 'work_locations': ['a']}
    ],
    'gardener': [
        {'name': 'Sam', 'location': '789 Willow St', 'work_locations': ['a']}
    ]
}

# User registration
print("Register a new user:")
username = input("Enter username: ")
password = input("Enter password: ")
location = input("Enter location: ")

if username in users:
    print("User already exists.")
else:
    users[username] = {
        'password': password,
        'location': location,
        'services_hired': []
    }
    print("User registered successfully.")

# User login
print("\nLogin user:")
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]['password'] == password:
    print("Login successful.")
else:
    print("Invalid username or password.")
    exit()

# User options menu
while True:
    print("\nOptions:")
    print("1. Hire a service provider   2. View bookings   3. Cancel a booking   4. Logout")
    choice = input("Enter your choice: ")
    if choice == '1':
        # Hire a service provider
        print("\nHire a service provider:")
        service_type = input("Enter service type to hire (plumber/electrician/maid/gardener): ")

        if username not in users:
            print("User not found.")
        elif service_type not in service_providers:
            print("Invalid service type.")
        else:
            user_location = users[username]['location']
            available_providers = [provider for provider in service_providers[service_type] if user_location in provider['work_locations']]
            
            if not available_providers:
                print(f"No {service_type}s available in your location.")
            else:
                provider = available_providers[0]
                # Get current date
                booking_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                users[username]['services_hired'].append({'type': service_type, 'provider': provider, 'date': booking_date})
                service_providers[service_type].remove(provider)
                print(f"{provider['name']} hired as {service_type}.")
    
    elif choice == '2':
        # View bookings
        print("\nView bookings:")
        if username not in users:
            print("User not found.")
        else:
            bookings = users[username]['services_hired']
            if not bookings:
                print("No bookings found.")
            else:
                for booking in bookings:
                    print(f"Service Type: {booking['type']}, Provider Name: {booking['provider']['name']}, Provider Location: {booking['provider']['location']}, Date: {booking['date']}")
    
    elif choice == '3':
        # Cancel a booking
        print("\nCancel a booking:")
        service_type = input("Enter service type to cancel (plumber/electrician/maid/gardener): ")

        if username not in users:
            print("User not found.")
        else:
            services_hired = users[username]['services_hired']
            for booking in services_hired:
                if booking['type'] == service_type:
                    services_hired.remove(booking)
                    service_providers[service_type].append(booking['provider'])
                    print(f"{booking['provider']['name']} booking canceled.")
                    break
            else:
                print(f"No {service_type} booked.")
    
    elif choice == '4':
        # Logout
        print("Logging out...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
