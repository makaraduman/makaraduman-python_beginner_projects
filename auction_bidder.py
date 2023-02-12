from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Wlecome to the secret auction program.")

bidders = {}
new_bidder = True
while new_bidder:
    #Name of the bidder & Bid ammount
    name = input("What is your name?: ").title()
    bid_amount = int(input("What is your bid?: $"))
    # Add every bidder to the bidders dictionary
    bidders[name] = bid_amount
    
    new_bidder = input("Are ther any other bidders? Type 'yes' or 'no'. ").lower()
    max_bid = max(bidders.values())
    max_bidder = max(bidders, key=bidders.get)
    if new_bidder == "no":
        new_bidder = False
        print(f"The winner is {max_bidder} with a bid of ${max_bid}")
        
    else:
        clear()
