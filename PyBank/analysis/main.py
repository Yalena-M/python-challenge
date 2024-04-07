import os
import csv

csv_file_path = os.path.join("..", "Resources", "budget_data.csv")
csv_file_path = 'C:\\Users\\jacya\\.ssh\\.ssh\\Starter_Code\\python-challenge\\PyBank\\Resources\\budget_data.csv'

# The total number of months included in the dataset
def count_months(csv_file_path):
    months = set()
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            month = row[0][:6]
            months.add(month)
    total_months = len(months)
    return total_months

total_months_count = count_months(csv_file_path)
print("Total Months:", total_months_count)

# The net total amount of "profit/losses" over the entire period
def calculate_net_total(csv_file_path):
    net_total = 0
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            amount = float(row[1])
            net_total += amount
    return net_total

total_amount = calculate_net_total(csv_file_path)
print("Net Total:", total_amount)

# The changes in "profit/losses" over the entire period, and then the average of those changes
def changes_average(csv_file_path):
    changes = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        previous_amount = None
        for row in csv_reader:
            amount = float(row[1])
            if previous_amount is not None:
                change = amount - previous_amount
                changes.append(change)
            previous_amount = amount

    average_change = sum(changes) / len(changes) if len(changes) > 0 else 0
    return changes, average_change

changes, average_change = changes_average(csv_file_path)
print("Average Change:", average_change)

# The greatest increase in profits (date and amount) over the entire period
def greatest_increase(csv_file_path):
    max_increase = float("-inf")
    max_increase_date = None
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        previous_amount = None
        previous_date = None
        for row in csv_reader:
            date = row[0]
            amount = float(row[1])
            if previous_amount is not None:
                increase = amount - previous_amount
                if increase > max_increase:
                    max_increase = increase
                    max_increase_date = date
            previous_amount = amount
    return max_increase_date, max_increase

max_increase_date, max_increase = greatest_increase(csv_file_path)
if max_increase_date is not None:
    print(f"Greatest increase in profits occurred on {max_increase_date} with an amount of {max_increase}")
else:
    print("No data available.")

# The greatest decrease in profits (date and amount) over the entire period
def greatest_decrease(csv_file_path):
    max_decrease = float("inf")
    max_decrease_date = None
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        previous_amount = None
        previous_date = None
        for row in csv_reader:
            date = row[0]
            amount = float(row[1])
            if previous_amount is not None:
                decrease = previous_amount - amount
                if decrease < max_decrease:
                    max_decrease = decrease
                    max_decrease_date = date
            previous_amount = amount
    return max_decrease_date, max_decrease

max_decrease_date, max_decrease = greatest_decrease(csv_file_path)
if max_decrease_date is not None:
    print(f"Greatest decrease in profits occurred on {max_decrease_date} with an amount of {max_decrease}")
else:
    print("No data available.")
