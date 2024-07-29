class Auction:
    def __init__(self, item, starting_price):
        self.item = item
        self.starting_price = starting_price
        self.highest_bid = starting_price
        self.highest_bidder = None
        self.bids = []

    def place_bid(self, user, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.highest_bidder = user.username

            if user.username in [username for username, _ in self.bids]:
                for i, (username, _) in enumerate(self.bids):
                    if username == user.username:
                        self.bids[i] = (user.username, bid_amount)
                        break
            else:
                self.bids.append((user.username, bid_amount))

            user.bids[self.item] = bid_amount
            print(f"New highest bid of {bid_amount} by {user.username}")
        else:
            print("Bid is too low, please place a higher bid.")

    def show_bids(self):
        if not self.bids:
            print("No bids placed yet.")
        else:
            print("All Bids:")
            for username, bid_amount in self.bids:
                print(f"{username}: {bid_amount}")

    def end_auction(self):
        if self.highest_bidder:
            print(f"Auction ended. The winner is {self.highest_bidder} with a bid of {self.highest_bid}.")
        else:
            print("Auction ended with no bids.")
