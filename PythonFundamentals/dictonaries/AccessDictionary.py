# Define a dictionary with personal information
my_dict = {
    "Name": "Tania",          # Person's name
    "Company": "Academy",       # Company name
    "University": "BUBT",        # University name
    "Phone": "01855454555",    # Phone number
    "Batch": 43                # Batch number
}

# Access an item by key using square bracket notation
print(my_dict["University"])   # Output: DIU

# Access an item using get() method
print(my_dict.get("Batch"))    # Output: 43