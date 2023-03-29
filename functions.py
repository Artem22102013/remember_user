import os
import json

def add_username(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            usernames = json.load(f)
    else:
        usernames = {}
    name = input("Enter a username: ")
    password = input("Enter a password: ")
    usernames[name] = password
    with open(filename, "w") as f:
        json.dump(usernames, f)
    print(f"Username '{name}' added successfully.")

def get_saved_usernames(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            usernames = json.load(f)
        return list(usernames.keys())
    else:
        return []

def reset_usernames(filename, username=None):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            usernames = json.load(f)
        if username is None:
            os.remove(filename)
            print("All usernames reset successful.")
        else:
            try:
                del usernames[username]
                with open(filename, "w") as f:
                    json.dump(usernames, f)
                print(f"Username '{username}' reset successful.")

            except KeyError:
                print(f"Username '{username}' not found.")
    else:
        print("No saved usernames to reset.")

filename = "usernames.json"

saved_usernames = get_saved_usernames(filename)
if saved_usernames:
    print("Welcome back, users:")
    for username in saved_usernames:
        if username != "Admin":
            print(username)
        else:
            print("                  ***")
            print("PLEASE ENJOY OURS PROGRAMM THAT WE'VE MADE FOR YOU!")
            print("                  ***")
else:
    print("No saved usernames found.")

while True:
    command = input("Enter a command (add to add a username, reset to reset usernames, reset [username] to reset a specific username, exit to exit the program): ")
    print("To Exit, please use '^C'.")
    if command == "add":
        add_username(filename)
    elif command == "reset":
        reset_usernames(filename)
    elif command.startswith("reset "):
        username = command.split(" ")[1]
        reset_usernames(filename, username)
    elif command == "exit":
        break
    else:
        print("Invalid command.")

print("Program terminated.")
