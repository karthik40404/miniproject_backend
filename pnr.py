from datetime import datetime
events=[]
while True:
    print("\n Personal Note Reminder ")
    print("1. Add Event")
    print("2. View Events")
    print("3. Delete Event")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        date=input("Enter event date (DD-MM-YYYY): ")
        try:
            datetime.strptime(date, '%d-%m-%Y')  
            event=input("Enter event description: ")
            events.append({'date': date, 'event': event})
            print(f"Event '{event}' added on {date} successfully!")
        except ValueError:
            print("Invalid date format.")
    elif choice==2:
        if not events:
            print("No events available.")
        else:
            for event in events:
                print(f"Date: {event['date']}, Event: {event['event']}")
    elif choice==3:
        date=input("Enter event date to delete (DD-MM-YYYY): ")
        event=input("Enter event description to delete: ")
        events=[e for e in events if not (e['date'] == date and e['event'] == event)]
        print(f"Event '{event}' on {date} deleted successfully!")
    elif choice==4:
        print("Exiting the program....")
        break
    else:
        print("Invalid choice.")



# '''continue'''
# for i in range(10):
#         if i==5:
#                 continue
#         print(i)

# '''break'''
# for i in range(10):
#         if i==5:
#                 break
#         print(i)
