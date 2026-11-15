import csv
from datetime import datetime, timedelta


def is_high_amount(amount):
    return amount >= 1000


def is_country_mismatch(country, home_country):
    return country != home_country


def parse_timestamp(timestamp):
    return datetime.fromisoformat(timestamp)


def is_high_velocity(transactions):
    time_window = timedelta(minutes=10)
    customer_counts = {}
    customer_times = {}

    for transaction in transactions:
        transaction_time = parse_timestamp(transaction["timestamp"])
        window_start = transaction_time - time_window
        customer_id = transaction["user_id"]

        if customer_id not in customer_times:
            customer_times[customer_id] = []

        customer_times[customer_id].append(transaction_time)

        recent_times = [
            time for time in customer_times[customer_id]
            if window_start <= time <= transaction_time
        ]

        customer_counts[customer_id] = len(recent_times)

        if customer_counts[customer_id] >= 3:
            return True

    return False

if __name__ == "__main__":
    first_time = parse_timestamp("2026-10-01T12:05:00")
    second_time = parse_timestamp("2026-10-01T12:09:00")

    time_difference = second_time - first_time

    print("First transaction:", first_time)
    print("Second transaction:", second_time)
    print("Time difference:", time_difference)

    time_window = timedelta(minutes=10)
    print("Within 10 minutes:", time_difference <= time_window)

    with open("data/transactions.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        transactions = list(reader)

    velocity_detected = is_high_velocity(transactions)

    print("High velocity detected:", velocity_detected)

    normal_transactions = [
        transaction for transaction in transactions
        if transaction["user_id"] == "U001"
    ]

    print("Normal activity detected as high velocity:", is_high_velocity(normal_transactions))

    spaced_transactions = [
        {"user_id": "U999", "timestamp": "2026-10-01T09:00:00"},
        {"user_id": "U999", "timestamp": "2026-10-01T09:20:00"},
        {"user_id": "U999", "timestamp": "2026-10-01T09:40:00"}
    ]

    print("Spaced transactions high velocity:", is_high_velocity(spaced_transactions))