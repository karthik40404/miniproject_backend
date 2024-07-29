from auction_system import AuctionSystem
from admin import Admin

def main():
    auction_system = AuctionSystem()
    auction = auction_system.create_auction("Kerala Blasters Ticket", 500)
    current_user = None
    
    admin_user = Admin()
    admin_logged_in = False

    while True:
        print("\nAuction System Menu")
        print("1. Register")
        print("2. Login")
        print("3. Place Bid")
        print("4. Admin Login")
        print("5. View All Bids (Admin)")
        print("6. View Users (Admin)")
        print("7. End Auction")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            auction_system.register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = auction_system.login_user(username, password)
            if user:
                current_user = user

        elif choice == "3":
            if current_user:
                bid_amount = float(input("Enter your bid amount: "))
                auction.place_bid(current_user, bid_amount)
            else:
                print("Please log in first to place a bid.")

        elif choice == "4":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            admin_logged_in = admin_user.login(username, password)

        elif choice == "5":
            if admin_logged_in:
                admin_user.view_all_bids(auction_system)
            else:
                print("Please log in as admin first.")

        elif choice == "6":
            if admin_logged_in:
                admin_user.view_users(auction_system)
            else:
                print("Please log in as admin first.")

        elif choice == "7":
            auction.end_auction()

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please try again.")

