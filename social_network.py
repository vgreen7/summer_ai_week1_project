#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            
            user = ai_social_network.create_account()
            

        elif choice == "2":
            #Allows for switch in ui
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "6":
                    break
                if inner_menu_choice == "1":
                    ai_social_network.edit_details(user)
                    break
                if inner_menu_choice == "2":
                    ai_social_network.add_friends(user)
                    break
                if inner_menu_choice == "4":
                    ai_social_network.show_friends(user)
                if inner_menu_choice == "3":
                    ai_social_network.block_friend(user)
                #else:
                    #inner_menu_choice = social_network_ui.manageAccountMenu()
                break

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
