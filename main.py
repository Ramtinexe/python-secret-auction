import os
# ASCII art displayed at the start of the program
art = '''
  
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
print(art)
print("Welcome to the secret auction program!")

# Dictionary used to store each bidder's name and bid
bidders = {}
continue_flag = True

# Finds and displays the bidder with the highest bid
def find_highest_bidder(bids):
    winner_bid = 0
    winner_name = ""
    # Check each bidder and compare their bid with the current highest bid
    for key in bids:
        if bids[key] > winner_bid:
            winner_bid = bids[key]
            winner_name = key

    print(f"the winner is {winner_name} with a bid of ${winner_bid}")


# Continue collecting bids until there are no more bidders
while continue_flag:
    name = input("Please enter your name: ")
    # Make sure the bid is a valid number
    try:
        bid = int(input("Please enter your bid: $ "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    # Store the bidder and their bid in the dictionary
    bidders[name] = bid
    # Ask if another bidder wants to participate
    other_bidders = input("Are there any other bidders? (y/n) ").lower()
    if other_bidders == "y":
        # Clear the console before the next bidder enters their bid
        continue_flag = True
        os.system("cls" if os.name == "nt" else "clear")

    elif other_bidders != "n" and other_bidders != "y":
        # Stop the program if the user enters an invalid option
        continue_flag = False
        print("Please enter a valid input.")
    else:
        # No more bidders, so find and display the winner
        continue_flag = False
        find_highest_bidder(bidders)
        input("Press enter to exit...")

