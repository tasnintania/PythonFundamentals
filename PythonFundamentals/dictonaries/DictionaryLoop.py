# Define a dictionary with personal information
my_dict = {
    "Name": "Tania",          # Person's name
    "Company": "Academy",       # Company name
    "University": "BUBT",        # University name
    "Phone": "0184555525",    # Phone number
    "Batch": 43                # Batch number
}

# Print all key-value pairs as a view object of tuples
print(my_dict.items())

# Iterate over dictionary keys and print key-value pairs
for value in my_dict:
    print(f"{value} : {my_dict[value]}")

# Iterate over dictionary key-value pairs directly using items()
for key, value in my_dict.items():
    print(f"{key} : {value}")