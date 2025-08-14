# # TODO-1: Ask the user for input
# name = input("Enter your name: ")
# bid = int(input("Enter your bid amount: $"))
# print("\n" * 20)
# # TODO-2: Save data into dictionary {name: price}
# bids = {}
# # TODO-3: Whether if new bids need to be added
# while input("Is there any other bidder? Please type 'Yes' or 'No': ").lower() == 'yes':
#     name = input("Enter your name: ")
#     bid = int(input("Enter your bid amount: $"))
#
#     bids[name] = bid #save the new bid amount into the dict
#     print("\n" * 20)
#
# # TODO-4: Compare bids in dictionary
# highest_bid = 0
# highest_bidder = ""
#
# for bidder in bids:
#     if bids[bidder] > highest_bid:
#         highest_bid = bids[bidder]
#         highest_bidder = bidder
#         print("\n" * 20)
#         print(f"The winner is {highest_bidder} with a bid of: ${highest_bid}")
#
#
#
#
#

def find_the_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder
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




