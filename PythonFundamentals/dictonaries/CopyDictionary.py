# Define a dictionary with personal information
my_dict = {
    "Name": "Tania",          # Person's name
    "Company": "Academy",       # Company name
    "University": "BUBT",        # University name
    "Phone": "0188445461",    # Phone number
    "Batch": 43                # Batch number
}

# Create a copy of the dictionary using the copy() method
copied_dict = my_dict.copy()
# Print the copied dictionary
print(f"Copied Dictionary: {copied_dict}")

# Create another copy of the dictionary using the dict() constructor
copied_dict2 = dict(my_dict)
# Print the second copied dictionary
print(f"Copied Dictionary: {copied_dict2}")