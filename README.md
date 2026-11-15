# fraud-risk-ops-lab
Beginner transaction monitoring and fraud risk scoring lab.

## Project Overview

The Fraud & Risk Operations Lab is a beginner-friendly project that demonstrates how financial transactions can be monitored for potentially suspicious activity.

The project uses fictional transaction data to explore fraud detection concepts, including high-dollar transactions, geographic mismatches, and transaction velocity.

The goal is to develop a Python-based monitoring system that assigns risk scores to transactions and generates a case queue for analyst review.

All transaction data in this repository is synthetic and does not contain real customer or financial information.

## Transaction Dataset

The project uses a synthetic CSV dataset containing 10 financial transactions, stored in `data/transactions.csv`.

Each transaction includes the following fields:

| Field | Description |
|---|---|
| `transaction_id` | Unique identifier for each transaction |
| `user_id` | Fictional customer identifier |
| `timestamp` | Date and time of the transaction |
| `amount` | Transaction amount in USD |
| `country` | Country where the transaction occurred |
| `home_country` | Customer's home country |
| `merchant_category` | Type of merchant involved in the transaction |

The dataset includes examples of high-dollar transactions, country mismatches, and multiple transactions occurring within a short time period. These examples will be used to test the fraud monitoring rules developed later in the project.


## Python Transaction Monitoring

This project includes a Python script that reads and analyzes a synthetic transaction dataset.

The script is located at `src/load_transactions.py`.

### Current Features

- Reads transaction data from a CSV file using Python's built-in `csv` module.
- Processes transactions using `csv.DictReader`.
- Converts transaction amounts from text into numeric values.
- Displays transaction IDs, customer IDs, and transaction amounts.
- Identifies transactions of $1,000 or more.
- Counts the total number of transactions processed.
- Counts the number of high-amount alerts generated.

### Running the Script

From the project's root directory, run:

```bash
python3 src/load_transactions.py
```

### Example Results

The current synthetic dataset contains 10 transactions.

```text
Total transactions: 10
High amount alerts: 2
```

The following transactions trigger the high-amount monitoring rule:

| Transaction ID | Amount | Alert |
|---|---:|---|
| T1003 | $1,450.00 | HIGH AMOUNT ALERT |
| T1008 | $2,300.00 | HIGH AMOUNT ALERT |

### Monitoring Disclaimer

All transaction data in this project is synthetic and used for educational purposes.

A monitoring alert does not confirm fraudulent activity. Alerts identify transactions that may require additional investigation.
