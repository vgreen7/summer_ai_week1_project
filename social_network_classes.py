# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
from unicodedata import name


class SocialNetwork:
 
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here

        global username
        name = input("What is your name?")
        username = name

        global age
        years = input("What is your age?")
        age = years

        u1 = Person(username, age)
        #listofpeople = self.list_of_people.append(name)
        #print(listofpeople)
        u1.printFunc()
        return u1
        

    ## For editing account information
    def edit_details(self, p1):
       
        currentName = p1.getName()
        currentAge = p1.getAge()
        print("Would you like to update your name or age? (n for name, a for age)")
        print("Your current name and name is " + currentName + " and your current age is " + currentAge)

        answer = input("n or a")

        if answer == "n":
            updatedName = input("What would you like your updated name to be?")
            p1.setName(updatedName)
            newName = p1.getName()
            print("your name is now " + newName)
            print(newName)
            username = newName
            
        elif answer == "a":
            updatedAge = input("What would you like your updated age to be?")
            p1.setAge(updatedAge)
            newAge = p1.getAge()
            print("Your name is now " + newAge)
            print(newAge)
            age = newAge
        
    
    def add_friends(self, p1):
        newFriend = input("Please provide the name of the friend you would like to add: ")
        p1.addFriend(newFriend)
        print("Your friend " + newFriend + " has been added!")

    def show_friends(self, p1):
        friendList = p1.getFriend()
        print(friendList)

    def block_friend(self, p1):
        blockedFriend = input("Which friend would you like to block?")
        friendList = p1.getFriend()
        friendList.remove(blockedFriend)
        print(blockedFriend + " has been removed.")

    def send_message(self, p1):
        friendList = p1.getFriend()
        print("List of friends: ")
        print(friendList)
        sendTo = input("Which friend would you like to send your message to?")
        message = input("What message would you like to send?")
        p1.addMessage(message)

    def view_message(self, p1):
        sentMessages = p1.getSentMessage()
        print(sentMessages)
        

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.inbox = []
        self.sentmessages = []

    def printFunc(self):
        print("Userneam: " + self.id + ", " + "Age: " + self.year)

    def getName(self):
        return self.id

    def getAge(self):
        return self.year

    def setAge(self, x):
        self.year = x

    def setName(self, x):
        self.id = x

    def addFriend(self, friend):
        self.friendlist.insert(0, friend)

    def getFriend(self):
        return self.friendlist

    def addMessage(self, message):
        self.sentmessages.insert(0, message)
    
    def getSentMessage(self):
        return self.sentmessages