def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:        
        return "You have to input name and phone"    
    name, phone = args
    if name in contacts:
        return 'such a record exists. Re-record?'
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        return 'No such record exists'
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if not args[0] in contacts:
        return 'No such record exists'
    return contacts[args[0]]

def show_all(contacts):
    contacts_string = ''
    if len(contacts) == 0:
        return 'No such record exists'
    for name, phone in contacts.items():
        contacts_string += f"{name}: {phone}\n"
    return contacts_string

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()