from observerPattern import *
class User:
    def __init__(self, userName, password):
        self.userObservable = userObservable
        self.Observer = Observer
        self.userName=userName
        self.password=password
        self.online = True

    def follow (self, other_user):
        if self.online:
            other_user.userObservable.attach(other_user, self) # user enters to the observers (followers) list of otherUser

    def unfollow (self, other_user):
        if self.online:
            other_user.userObservable.remove(other_user, self) # user left the observers (followers) list of otherUser


    def comment (self, other_user, comment_txt):
        if self.online:
            other_user.Observer.gotCommentNotification(other_user, self, comment_txt)

    def print_notifications(self):
        Observer.StringNotifications()

    def __str__(self):
        return f"User name:{self.userName}, Number of Posts:, Number of followers:{self.userObservable.getNum()}"





