from User import *

# a Singelton design pattern
class SocialNetwork:
    # variables of the Network class
    _instance = None

    def __init__(self, network_name):
        self.users_names = set()
        self.users = set()
        self.network_name = network_name

    def __new__(cls, network_name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.network_name = network_name
            print("A new social network " + network_name + " was created!")
        return SocialNetwork._instance

    # in the user's tap "Sign up"
    # gets the instance of the network that has been created, name and password (that the user put)
    def sign_up(self, user_name, password):
        while self.users_names.__contains__(user_name):
            name = input("User name is in use")
        while len(password) < 4 or len(password) > 8:  # check if the password and the name are legal
            password = input("Password should be 4-8 characters long")

        # now, that the name and password legal, we can create the user
        new_user = User(user_name, password)
        self.users_names.add(user_name)  # add the user to the set of all user's name
        self.users.add(new_user)
        new_user.online = True
        # initilize the user's online status to be True

    def log_in(self, user_name, password):
        for user in self.users:
            if user.user_name == user_name:
                if user.password == password:
                    user.online = True
                    print(user.user_name + " connected")
            else:
                print("password or user name not correct")

    def log_out(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                user.online = False
                print(user_name + " disconnected")

