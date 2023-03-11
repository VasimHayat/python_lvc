# Initialize an empty dictionary to store the counts
response_counts = {}

# Loop through the responses and update the counts
responses = ['Yes', 'No', 'Maybe', 'Yes', 'No', 'Yes']
for response in responses:
    if response in response_counts:
        response_counts[response] += 1
    else:
        response_counts[response] = 1

# Print the counts
for resp, count in response_counts.items():
    print(f"this is the output : {resp}: {count}")