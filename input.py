# user_text = input('Enter some text: ')

# print(user_text.upper())

# user_number = input("What do you want to double? ")

# print(int(user_number) * 2)

# First ask for some text, and then prompt "Enter 1 to uppercase and 2 to lowercase: " and then either upper or lowercase it

user_text = input("Enter some text: ")

cap_or_not = input("Enter 1 to uppercase and 2 to lowercase: ")


if cap_or_not == "1":
    print(user_text.upper())
elif cap_or_not == "2":
    print(user_text.lower())
else:
    print("Please try again with a valid number.")