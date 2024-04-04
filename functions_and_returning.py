def double(number):
    return number * 2
    
new_number = double(5)

print(new_number)

#  Create a function that returns a string in all caps (you'll have to google this)

def capitol(string):
    return string.upper()

new_string = capitol("Kevin was here!")

print(new_string)

names = ["nick", "Jane", "sara"]

for name in names:
    print(capitol(name))