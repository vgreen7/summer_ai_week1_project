# You can implement user interface functions here.
from social_network_classes import SocialNetwork


def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block friend")
    print("4. View all my friends")
    print("5. Send message")
    print("6. View my sent messages")
    print("7. View my inbox")
    print("8. <- Go back ")
    return input("Please Choose a number: ")

def editDetails():
    print("")
    print("edit details ui switch")