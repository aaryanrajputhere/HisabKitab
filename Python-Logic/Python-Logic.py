from datetime import datetime
import pandas as pd
from xlsxwriter import workbook

# Function to split expenses among participants
def split_expenses(amount, paid_by, people_involved, split_option, purpose, trip_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    amounts_split = []
    if split_option == '1':
        # Split equally
        num_people_involved = len(people_involved)
        split_amount = amount / num_people_involved
        amounts_split = [split_amount] * num_people_involved
        net_amounts[paid_by] -= amount
    elif split_option == '2':
        # Split unequally
        amounts_split = input("Enter the amounts to be split for each person (comma-separated): ").split(',')
        amounts_split = [float(amount) for amount in amounts_split]
        if sum(amounts_split) != amount:
            print("Error: Sum of amounts provided should match the total amount.")
            return
        net_amounts[paid_by] -= amount
    else:
        print("Invalid choice for split option.")

    for i, person_id in enumerate(people_involved):
        net_amounts[person_id] += amounts_split[i]
        transactions.append({
            'trip_name': trip_name,
            'timestamp': timestamp,
            'paid_by': paid_by,
            'amount': amounts_split[i],
            'people_involved': [person_id],
            'purpose': purpose
        })
        # Calculate and update social score
        social_score[paid_by] = calculate_social_score(social_score[paid_by], 0, amounts_split[i], amount)


# Function to calculate and store payments
def calculate_payments():
    for person_id, net_amount in net_amounts.items():
        if net_amount < 0:
            for creditor_id, creditor_amount in net_amounts.items():
                if creditor_amount > 0:
                    payment = min(-net_amount, creditor_amount)
                    payments.append({
                        'from': creditor_id,
                        'to': person_id,
                        'amount': payment
                    })
                    net_amounts[creditor_id] -= payment
                    net_amounts[person_id] += payment


def pay():
    Pay_back = input("Enter repayment (who paid, to whom (ID)): ").split(',')
    repay_amount = float(input("Enter the amount: "))

    paid_b=int(Pay_back[0])
    paid_t=int(Pay_back[1])

    net_amounts[paid_b]-=repay_amount
    net_amounts[paid_t]+=repay_amount

    repay_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Calculate and update social score
    social_score[paid_b] = calculate_social_score(social_score[paid_b], 0, repay_amount, repay_amount)
    print("New Social Score of", participants[paid_b]['name'], "is ", social_score[paid_b])

def calculate_social_score(initial_score, time_difference, amount_repaid, total_amount):
    # Define weightage for time and amount factors
    time_weightage = 0  # Adjust the weightage based on your preference
    amount_weightage = 0.5  # Adjust the weightage based on your preference

    # Introduce a decay factor for time (adjust the decay rate based on your preference)
    decay_factor = 0.5

    # Calculate time factor (negative value) with decay
    time_factor = (time_weightage) * ((1 / (1 + time_difference))) * ((1 - decay_factor * time_difference))

    # Calculate amount factor (positive value)
    amount_factor = amount_weightage * (amount_repaid / total_amount)

    # Define maximum increase per repayment
    max_increase = 5  # Adjust as needed

    # Calculate social score increase
    social_score_increase = min(max_increase, amount_factor - time_factor)
    
    # Calculate new social score
    new_social_score = initial_score + social_score_increase

    # Ensure the social score is within the desired range (e.g., 0 to 100)
    new_social_score = max(0, min(100, new_social_score))

    return new_social_score



# Initialize variables
next_id = 1
participants = {}
net_amounts = {}
transactions = []
payments = []
social_score = {}


# Get trip details
trip_name = input("Enter the name of the Trip: ")

# Get participant details
while True:
    name = input("Enter the Name of the Participant (or 'exit' to stop): ")

    if name.lower() == 'exit':
        break

    mobile_number = input("Enter the Mobile Number for the Participant: ")
    upi_id = input("Enter the UPI ID for the Participant: ")

    participants[next_id] = {'name': name, 'mobile_number': mobile_number, 'upi_id': upi_id}
    net_amounts[next_id] = 0
    social_score[next_id] = 50
    print(f"Participant {name} has been assigned ID: {next_id}")
    next_id += 1

# Start recording transactions
while True:
    print("\nTrip Options:")
    print("1. Add Transaction")
    print("2. Finish Trip and Calculate Payments")
    print("3. Pay back and settle")
    print("4. End ")
    trip_option = input("Enter your choice (1/2/3/4): ")

    if trip_option == '1':
        # Get transaction details
        for key, inner_dict in participants.items():
            if 'name' in inner_dict:
                print(f"Unique ID: {key}, Name: {inner_dict['name']}")
                
        paid_by_name = input("Enter the person who paid (by ID): ")
        paid_by = int(paid_by_name)
        amount = float(input("Enter the amount: "))
        split_option = input("Split equally (1) or unequally (2): ")
        purpose = input("Enter the purpose of the transaction: ")

        for key, inner_dict in participants.items():
            if 'name' in inner_dict:
                print(f"Unique ID: {key}, Name: {inner_dict['name']}")

        people_involved_names = input("Enter the people involved (comma-separated by ID): ").split(',')
        people_involved = [int(person_id) for person_id in people_involved_names]

        # Split the expenses
        split_expenses(amount, paid_by, people_involved, split_option, purpose, trip_name)
        print("\nTransaction added successfully!\n")
        print(net_amounts)

    elif trip_option == '2':
        print(net_amounts)
        calculate_payments()

    elif trip_option == '3':
        pay()

    elif trip_option == '4':
        print(net_amounts)
        break

    # elif trip_option == '2':
    #     calculate_payments()
    #     break

# Print information for payment
print("\nPayments:")
for payment in payments:
    from_name = participants[payment['from']]['name']
    to_name = participants[payment['to']]['name']
    print(f"{from_name} owes {to_name} Rs {round(payment['amount'],2)}")

# Display all transactions
print(f"\nAll Transactions for the trip: {trip_name}")
for transaction in transactions:
    paid_by_name = participants[transaction['paid_by']]['name']
    people_involved_names = [participants[person_id]['name'] for person_id in transaction['people_involved']]
    print(f"Timestamp: {transaction['timestamp']}, Paid By: {paid_by_name}, Amount: {round(transaction['amount'], 2)}, People Involved: {people_involved_names}, Purpose: {transaction['purpose']}")

# Convert participant IDs to names in transactions
transactions_readable = []
for transaction in transactions:
    paid_by_name = participants[transaction['paid_by']]['name']
    people_involved_names = [participants[person_id]['name'] for person_id in transaction['people_involved']]
    transactions_readable.append({
        'trip_name': transaction['trip_name'],
        'timestamp': transaction['timestamp'],
        'paid_by': paid_by_name,
        'amount': round(transaction['amount'],2),
        'people_involved': people_involved_names,
        'purpose': transaction['purpose']
    })

# Convert participant IDs to names in payments
payments_readable = []
for payment in payments:
    from_name = participants[payment['from']]['name']
    to_name = participants[payment['to']]['name']
    payments_readable.append({
        'from': from_name,
        'to': to_name,
        'amount': round(payment['amount'],2)
    })

# Save readable payments to Excel
df_payments_readable = pd.DataFrame(payments_readable)
df_transactions_readable = pd.DataFrame(transactions_readable)
with pd.ExcelWriter(f'{trip_name}_transactions.xlsx', engine='xlsxwriter') as writer:
    df_transactions_readable.to_excel(writer, sheet_name='Transactions', index=False)
    df_payments_readable.to_excel(writer, sheet_name='Owes and Lends', index=False)
