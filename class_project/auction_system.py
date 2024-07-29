from user import User
from auction import Auction

class AuctionSystem:
    def __init__(self):
        self.users = {}
        self.auctions = []

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another.")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"User {username} logged in successfully.")
            return self.users[username]
        else:
            print("Invalid username or password.")
            return None

    def create_auction(self, item, starting_price):
        auction = Auction(item, starting_price)
        self.auctions.append(auction)
        print(f"Auction created for {item} starting at {starting_price}.")
        return auction
