import csv
from fraud_rules import is_high_amount, is_country_mismatch, is_high_velocity

print("Fraud & Risk Operations Lab")

file_path = "data/transactions.csv"

with open(file_path, "r", newline="") as file:
    print("Transaction file opened successfully!")
    reader = csv.DictReader(file)
        
    transaction_count = 0
    high_amount_count = 0
    country_mismatch_count = 0
    all_transactions = []
        
    for transaction in reader:
        all_transactions.append(transaction)

        amount = float(transaction["amount"])
        
        print(f"Transaction: {transaction['transaction_id']} | Customer: {transaction['user_id']} | Amount: ${transaction['amount']}")
        transaction_count += 1

        if is_high_amount(amount):
            print("  HIGH AMOUNT ALERT!")
            high_amount_count += 1
        if is_country_mismatch(transaction["country"], transaction["home_country"]):
            print("  COUNTRY MISMATCH ALERT!")
            country_mismatch_count += 1

    print("Total transactions:", transaction_count)
    print("High amount alerts:", high_amount_count)
    print("Country mismatch alerts:", country_mismatch_count)
    
    velocity_detected = is_high_velocity(all_transactions)
    print("High velocity detected:", velocity_detected)