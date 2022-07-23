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
        #User = Person()

        global username
        name = input("What is your name?")
        username = name


        global age
        years = input("What is your age?")
        age = years

        u1 = Person(username, age)

        u1.printFunc()



    ## For editing account information
    def edit_details(self):
        p1 = Person(username, age)
        currentName = p1.getName()
        currentAge = p1.getAge()
        print("Would you like to update your name or age? (n for name, a for age)")
        print("Your current name and name is " + currentName + "and your current age is " + currentAge)

        answer = input("n or a")

        if answer == "n":
            updatedName = input("What would you like your updated name to be?")
            print("your name is now" + updatedName)

        elif answer == "a":
            print("responded with n" )
        



class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def printFunc(self):
        print("Userneam: " + self.id + "Age: " + self.year)

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        #implement sending message to friend here
        pass

    def getName(self):
        return self.id

    def getAge(self):
        return self.year
