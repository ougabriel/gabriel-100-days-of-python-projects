from art import logo
print(logo)

def find_the_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder

            print("\n" * 20)
            print(f"The winner is {highest_bidder} with a bid of: ${highest_bid}")


bids = {}
should_continue = True
while should_continue:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount:$ "))
    bids[name] = bid

    to_continue_bid = input("Is there any other bidder? Type 'Yes' or 'No': ").lower()
    if to_continue_bid == "no":
        should_continue = False
        find_the_highest_bidder(bids)
    elif to_continue_bid == "yes":
        print("\n" * 20)
