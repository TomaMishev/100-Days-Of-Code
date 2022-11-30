from art import logo
import os


def clear(): os.system('cls')


print(logo)
print("Welcome to the secret auction program!")
auction_dict = {}
while True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    auction_dict[name] = int(bid)
    user_control = input("Are there any other bidders? Type 'yes' or 'no.\n")
    if user_control == 'yes':
        clear()
        continue
    else:
        break
biggest_bid = -1
biggest_bid_per_person = ""
for key in auction_dict:
    if biggest_bid <= auction_dict[key]:
        biggest_bid = auction_dict[key]
        biggest_bid_per_person = key
clear()
print(f"The winner is {biggest_bid_per_person} with a bid of ${biggest_bid}.")