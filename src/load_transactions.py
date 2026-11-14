import csv

print("Fraud & Risk Operations Lab")

file_path = "data/transactions.csv"

with open(file_path, "r", newline="") as file:
    print("Transaction file opened successfully!")
    reader = csv.DictReader(file)
        
    transaction_count = 0
    high_amount_count = 0
        
    for transaction in reader:
        amount = float(transaction["amount"])
        
        print(f"Transaction: {transaction['transaction_id']} | Customer: {transaction['user_id']} | Amount: ${transaction['amount']}")
        transaction_count += 1

        if amount >= 1000:
            print("  HIGH AMOUNT ALERT!")
            high_amount_count += 1

    print("Total transactions:", transaction_count)
    print("High amount alerts:", high_amount_count)
