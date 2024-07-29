class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "admin123"

    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Admin {username} logged in successfully.")
            return True
        else:
            print("Invalid admin username or password.")
            return False

    def view_users(self, auction_system):
        print("Registered Users:")
        for username in auction_system.users:
            print(username)

    def view_all_bids(self, auction_system):
        for auction in auction_system.auctions:
            print(f"Bids for {auction.item}:")
            auction.show_bids()
