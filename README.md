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

