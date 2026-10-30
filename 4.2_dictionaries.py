"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: information about a person's bank account
# 2. Process: the program asks the user five questions, stores the answers in a dictionary, reads and changes information, removes one field and displays the remaining fields
# 3. Out: tthe bank account information and its updated values
# 4. My object, my five fields, and why those: i chose the owern's name, balance, bank name, currency and account type because these are useful to decribe an account


# Your code below

owner = input("Enter your name: ")
balance = input ("Enter your account balance: ")
bank = input ("Enter your bank name: ")
currency = input ("Enter your currency: ")
account_type = input ("Enter your account type: ")


account = {
    "owner" : owner,
    "balance" : balance,
    "bank" : bank,
    "currency" : currency,
    "account_type" : account_type,
}

# read the information
print("The account owner's name is: ", account ["owner"])
print("The account balance is: ", account ["balance"])
print("The bank is: ", account ["bank"])
print("The currency is: ", account ["currency"])
print("The account type is: ", account ["account_type"])

# change one field
account["balance"] = "3000"

# remove one field

remove_type = account.pop ("account_type")
print("The account type was: ", remove_type)

# display every remaining field
for field, value in account.items():
    print(field, ":", value)


