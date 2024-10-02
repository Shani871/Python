import re

def extract_information(text):
    # Regular expression patterns for phone numbers, email addresses, and postal addresses
    phone_pattern = r'\(\+\d{2}\) \d{10}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    postal_pattern = r'\d{1,5}\s[\w\s]+,\s[\w\s]+,\s[\w\s]+,\s\d{5}'

    # Extract phone numbers
    phone_numbers = re.findall(phone_pattern, text)

    # Extract email addresses
    email_addresses = re.findall(email_pattern, text)

    # Extract postal addresses
    postal_addresses = re.findall(postal_pattern, text)

    # Return extracted information
    return phone_numbers, email_addresses, postal_addresses

# Sample text data
text_data = """
Here are some contact details:
Phone: (+12) 1234567890, (+34) 9876543210
Emails: john.doe@example.com, jane_smith123@domain.co
Postal Addresses:
123 Main St, Springfield, IL, 62701
456 Elm St, Shelbyville, IL, 62565
"""

# Extract information from the text data
phone_numbers, email_addresses, postal_addresses = extract_information(text_data)

# Print the extracted information
print("Phone Numbers:")
for number in phone_numbers:
    print(number)

print("\nEmail Addresses:")
for email in email_addresses:
    print(email)

print("\nPostal Addresses:")
for address in postal_addresses:
    print(address)
