import self

from ex_2.User import User


#the network implementation
# implements by a Singelton design pattern

class SocialNetwork:

    #variables of the Network class
    _instance = None

    def __init__(self, name):
        self.name = name
        users_names = set()


    def __new__(self):
        if not self._instance is None:
            self._instance = object.__new__(self)          #If no network instance has been created yet
            print("A new social network "+self.name+" was created!")

        return self._instance



    #in the user's tap "Sign up"
    # gets the instance of the network that has been created, name and password (that the user put)
    def __add_user(self ,name, password):

        while(len(password) < 4 or len(password) >8):                    #check if the password and the name is legal
            password = input("Password should be 4-8 characters long")
        while(self.users_names.__contains__(name)):
            name = input("User name is in use")

        #now, that the name and password legal, we can create the user
        user = User(name, password)
        self.users_names.add(name)    #add the user to the set of all user's name
        user.__log_in                       #initilize the user's online status to be True


    def __log_in(user :User):
        if user.userName in self.users_names:
            user.online = True
            print(user.userName + " connected")


    def __log_out(self, user :User):
        if user.userName in self.users_names:
            user.online = False
        print(user.userName + " disconnected")


    def __is_online(user :User):
        if user.userName in self.users_names:
            return user.online

