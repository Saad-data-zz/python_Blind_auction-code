#import logo from art.py
from art import logo
import os
print(logo)
#HINT: You can call clear() to clear the output in the console.
#empty dictionary
bidding_record = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bidding_amount = bidding_record[bidder]
    if bidding_amount > highest_bid:
      highest_bid = bidding_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name_bidder = input("What is your name?: ")
  bidder_amount = int(input("What's your bid?=$"))
  bidding_record[name_bidder] = bidder_amount
  should_continue = input("Are there any other bidder's? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bidding_record)
  elif should_continue == "yes":
    clear()