import functions as fun

filename = "usernames.json"

saved_usernames = fun.get_saved_usernames(filename)
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
    command = input("Enter a command (add to add a username, reset to reset usernames, reset [username] to reset a specific username): ")
    if command == "add":
        fun.add_username(filename)
    elif command == "reset":
        fun.reset_usernames(filename)
    elif command.startswith("reset "):
        username = command.split(" ")[1]
        fun.reset_usernames(filename, username)
    else:
        print("Invalid command.")
