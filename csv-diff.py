import csv
import json

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def generate_diff_messages(old_data, new_data):
    messages = []
    for old_row, new_row in zip(old_data, new_data):
        diff = {}
        for key, value in new_row.items():
            if old_row.get(key) != value:
                diff[key] = {
                    "old_value": old_row.get(key),
                    "new_value": value
                }
        if diff:
            message = {
                "id": int(old_row.get("id")),
                "op": "u",
                "before": old_row,
                "after": new_row
            }
            print(message)
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            messages.append(message)
    return messages

def write_messages_to_file(messages, file_path):
    with open(file_path, 'w') as file:
        for message in messages:
            file.write(json.dumps(message) + '\n')

# Provide the file paths for the old and new versions of the CSV file
old_csv_file = 'old_data.csv'
new_csv_file = 'new_data.csv'

# Read the CSV files
old_data = read_csv(old_csv_file)
new_data = read_csv(new_csv_file)

# Generate diff messages
diff_messages = generate_diff_messages(old_data, new_data)

# Write the messages to a file
output_file = 'diff_messages.json'
write_messages_to_file(diff_messages, output_file)