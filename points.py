import argparse
import pandas as pd
from os.path import exists
import json


def spend_points(points_to_spend, transactions):
    
    # Create dictionary to store payer balances
    balances = {}
    
    # Sort transactions by timestamp (oldest first)
    transactions = transactions.sort_values('timestamp')
    
    for _, transaction in transactions.iterrows():
        
        payer = transaction['payer']
        points = transaction['points']
        
        # check and create entry for payer if payer does not exist in balances dictionary
        if payer not in balances:
            balances[payer] = 0
        
        if points >=0:
            # update the balance for the payer
            balances[payer] += points

            # check if there are enough points to spend
            if points_to_spend >= balances[payer]:
                # subtract points from balance and update points to spend
                points_to_spend -= balances[payer]
                balances[payer] = 0
            else:
                # update the balance for the payer
                balances[payer] -= points_to_spend
                points_to_spend = 0
        else:
            # add negative points back to points_to_spend 
            points_to_spend += -points
            
            # if payer has enough positive balance, subtract -ve points from the payer's balance
            if balances[payer] >= -points:
                balances[payer] += points
            else:
                # if payer does not have enough positive balance to offset the negative points, set balance for payer to 0
                balances[payer] = 0
    
    if points_to_spend != 0:
        print("Spending points according to given transactions file unsucessful!\nMaybe there are too many negative points")
    
    return balances


def display_balances(balances):
    print("Final Payer Balances: ")
    # Print the dictionary in json format
    print(json.dumps(balances, indent=4))


if __name__ == "__main__":
    
    # Set up command-line arguments parser
    parser = argparse.ArgumentParser(description="Compute total points to spend based on transactions history")
    parser.add_argument('-tf', '--transaction-filename', type=str, help='path to CSV file containing the transactions')
    parser.add_argument('-ps', '--points-to-spend', type=int, help='the number of points to spend')
    args = parser.parse_args()
    
    # Read program arguments from command-line
    points_to_spend = args.points_to_spend
    transactions_filename = args.transaction_filename
    
    # Assert program arguments are valid
    assert points_to_spend >=0, "The number of points to spend cannot be negative!"
    assert exists(transactions_filename), "The transaction filename does not exist!"
    
    # Display input
    print("Amount of points to spend: ", points_to_spend)
    print("Transactions file name: ", transactions_filename)
    
    # Read transactions from CSV file using pandas
    transactions = pd.read_csv(transactions_filename)
    
    # Calculate net balances per payer after spending points
    balances = spend_points(points_to_spend, transactions)
    
    # Display balances
    display_balances(balances)




