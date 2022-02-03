# this file shows use of dictionary comprehension

users = [
    (0, "Sam", "Password"),
    (1, "VD", "Vpass"),
    (2, "BK", "Bpass"),
    (3, "ND", "Npass")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)
username_input = input("Enter your user name:")
password_input = input("Enter your password:")

# this is important - use of underscore for not important unpacking
_, username, password = username_mapping[username_input]

if password_input == password:
    print("User login")
else:
    print("Login failed! Incorrect password")