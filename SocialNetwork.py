from User import User

# a Singelton design pattern (we want only one social network in run time)
class SocialNetwork:
    # make instance null
    _instance = None

    def __init__(self, network_name):
        self.users_names = set() #we used set() for make sure theres no same usernames
        self.users = [] #not set() too because we want to print users in order of their creation
        self.network_name = network_name

    def __new__(cls, network_name): #how we make singleton design pattern
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.network_name = network_name
            print("The social network " + network_name + " was created!")
        return SocialNetwork._instance

    # in the user's tap "Sign up"
    # gets name and password (that the user put) and check them
    def sign_up(self, user_name, password):
        while self.users_names.__contains__(user_name):
            user_name = input("User name is in use")
        while len(password) < 4 or len(password) > 8:  # check if the password and the name are legal
            password = input("Password should be 4-8 characters long")

        # now, that the name and password legal, we can create the user
        new_user = User(user_name, password)
        self.users_names.add(user_name)  # add the username to the set of all user's names
        self.users.append(new_user)  # add the user to the list of all users
        new_user.online = True
        return new_user

    def log_in(self, user_name, password):
        for user in self.users: #pass all the users and check if he has the username on the list if not throw Exception
            if user.user_name == user_name:
                if user.password == password: #check right password if not throw Exception
                    user.online = True
                    print(user.user_name + " connected")
                    return
                else:
                    raise Exception("password is wrong")
        raise Exception("user name doesn't exit")

    def log_out(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                user.online = False
                print(user_name + " disconnected")

    def __str__(self):
        tmp = (self.network_name+" social network:\n")
        for user in self.users:
            tmp+=user.__str__()+"\n"
        return tmp