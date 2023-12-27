from cryptography.fernet import Fernet


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
"""


def load_key():
    with open("password manager/key.key", "rb") as key_file:
        key = key_file.read()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password manager/password.txt", "r") as file:
         for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Name: {} | Password: {}".format(user,fer.decrypt(passw.encode()).decode()))


def add():
    name = input("Enter name: ")
    password = input("Enter password: ")
    with open("password manager/password.txt", "a") as file:
        file.write("{} | {}\n".format(name, fer.encrypt(password.encode()).decode()))
    print("Added Successfully ✅.")


def main():
    while True:
        choice = input("What do you want to do?('add', 'view' or 'q' for Quit.) \n")
        if choice == 'q':
            break
        elif choice == 'add':
            add()
        elif choice =='view':
            view()
        else:
            continue



if __name__ == "__main__":
    main()