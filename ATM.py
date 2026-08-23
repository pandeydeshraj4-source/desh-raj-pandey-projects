print("For accessing your Bank Details")
print("Enter your credentials")

Card_num = input("Enter your 12-digit card number: ").strip()
Card_holder = input("Enter the name of card holder: ").strip()
Mobile_num = input("Enter the mobile number linked to the Bank Account: ").strip()

# Standardized database with uniform key names across all records
database = [
    {
        "Card_holder": "Desh Raj Pandey",
        "Card_num": "123456789123",
        "Mobile_num": "9999999999",
        "Details": {
            "Name": "Desh Raj Pandey",
            "Bank name": "State Bank Of India",
            "Your Balance": "5,678"
        }
    },
    {
        "Card_holder": "Shiv Ram Pandey",  # Fixed key name
        "Card_num": "111111111111",     # Fixed key name
        "Mobile_num": "8888888888",     # Fixed key name
        "Details": {
            "Name": "Shiv Ram Pandey",
            "Bank name": "HDFC Bank",
            "Your Balance": "1,58,650"
        }
    }
]

# Search through the list of accounts
found_account = None

for account in database:
    if (
        account["Card_holder"].lower() == Card_holder.lower()
        and account["Card_num"] == Card_num
        and account["Mobile_num"] == Mobile_num
    ):
        found_account = account
        break

# Display results
if found_account:
    print("\n--- Account Details Found ---")
    for key, value in found_account["Details"].items():
        print(f"{key}: {value}")
else:
    print("\nInvalid input or details do not match.")