print("1. Add Donor\n2. View Donors\n3. Update Donor\n4. Delete Donor\n5. Exit")

donors = []

while True:
    print("Blood Bank Management System")
    print("1. Add Donor | 2. View Donors | 3. Update Donor | 4. Delete Donor | 5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        while True:
            donor_id = input("Enter Donor ID: ")
            if any(donor["id"] == donor_id for donor in donors):
                print("Donor ID already exists. Please enter a unique ID.")
            else:
                break
        
        name = input("Enter Donor Name: ")
        
        while True:
            blood_group = input("Enter Blood Group (O, A, B, AB): ").upper()
            if blood_group in ["O", "A", "B", "AB"]:
                break
            else:
                print("Invalid blood group. Please enter one of the following: O, A, B, AB.")
        
        contact = input("Enter Contact Number: ")
        donors.append({"id": donor_id, "name": name, "blood_group": blood_group, "contact": contact})
        print("Donor added successfully!\n")
    
    elif choice == '2':
        if donors:
            print("\n{:<10} {:<20} {:<15} {:<15}".format("ID", "Name", "Blood Group", "Contact"))
            print("-" * 60)
            for donor in donors:
                print("{:<10} {:<20} {:<15} {:<15}".format(donor['id'], donor['name'], donor['blood_group'], donor['contact']))
            print("")
        else:
            print("\nNo donors found!\n")
    
    elif choice == '3':
        donor_id = input("Enter Donor ID to update: ")
        for donor in donors:
            if donor["id"] == donor_id:
                print("Current Name: " + donor['name'])
                new_name = input("Enter new name (leave blank to keep current): ")
                donor["name"] = new_name or donor["name"]
                
                print("Current Blood Group: " + donor['blood_group'])
                while True:
                    new_blood_group = input("Enter new blood group (leave blank to keep current): ").upper()
                    if new_blood_group in ["", "O", "A", "B", "AB"]:
                        donor["blood_group"] = new_blood_group or donor["blood_group"]
                        break
                    else:
                        print("Invalid blood group. Please enter one of the following: O, A, B, AB.")
                
                print("Current Contact: " + donor['contact'])
                new_contact = input("Enter new contact (leave blank to keep current): ")
                donor["contact"] = new_contact or donor["contact"]
                
                print("Donor updated successfully!\n")
                break
        else:
            print("Donor not found!\n")
    
    elif choice == '4':
        donor_id = input("Enter Donor ID to delete: ")
        for donor in donors:
            if donor["id"] == donor_id:
                donors.remove(donor)
                print("Donor deleted successfully!\n")
                break
        else:
            print("Donor not found!\n")
    
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.\n")
