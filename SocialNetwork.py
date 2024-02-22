from User import *



'''We chose to implement SocialNetwork class - using the singleton design pattern
As we learned in the lecture,
Singleton is a creational design pattern that lets you ensure that a class has only one instance,
while providing a global access point to this instance.
The reason we used this specific design pattern is to force only one instance of SocialNetwork doring the program run,
As requested in the exercise instructions for this class
'''

class SocialNetwork:
    
    _instance = None    #initilize the instance represent a SocialNetwork to be none


    def __init__(self, network_name):
        self.users_names = set()          #create a set of users (in the SocialNetwork)
        self.users = set()                #create a set of users names (in the SocialNetwork)
        self.network_name = network_name  #gets a network name

    
    def __new__(cls, network_name):
        if cls._instance is None:                             #If a network instance hasn't been created yet, we allow to created one
            cls._instance = super().__new__(cls)              #create a SocialNetwork object
            cls._instance.network_name = network_name
            print("A new social network " + network_name + " was created!")  
        return SocialNetwork._instance                         #return the instance of SocialNetwork: none, or the only one object


    def sign_up(self, user_name, password):
        while self.users_names.__contains__(user_name):                   #Check that the user name entered not in use, as requestd
            name = input("User name is in use, try again")                           #gets input from the user until he get a legal user name
        while len(password) < 4 or len(password) > 8:                     #Check that the password entered in the legal size, as requestd
            password = input("Password should be 4-8 characters long, try again")    #gets input from the user until he get a legal password

        #user name and password are legal, we can create an user object
        new_user = User(user_name, password)
        self.users_names.add(user_name)  # add the user to the set of all user's name
        self.users.add(new_user)
        new_user.online = True
        # initilize the user's online status to be True

    def log_in(self, user_name, password):
        for user in self.users:                     
            if user.user_name == user_name:         #If the user belongs to users in SocialNetwork
                if user.password == password:       #And the password matches the username he entered
                    user.online = True                
                    print(user.user_name + " connected")
            else:
                print("password or user name not correct")   #Incorrect username or password

    def log_out(self, user_name):           
        for user in self.users:                  
            if user.user_name == user_name:      #disconnect only by user name
                user.online = False
                print(user_name + " disconnected")

