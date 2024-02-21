class userObservable:
    #userObservable is observable, and when updates about the user are updated, the state of userObservable changes.
    def __init__(self, userName):
        self.observers = [] # all the observers (followers) that get updates from this userObservable
        self.userName = userName

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            print(observer.name+" started following "+self.userName)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            print(observer.name+" unfollowed "+self.userName)

    def getNum(self):
        return self.observers.__sizeof__()

class Observer: #followers
    def __init__(self, userObservable, userName):
        self.userObservable = userObservable
        self.userName = userName
        self.notifications = []

    def gotLikeNotification(self, user):
        if self.userName != user.userName:
            self.notifications.append(f"{user.userName} liked your post")
            print("notification to"+self.userName+self.notifications.pop())

    def gotCommentNotification(self, user,comment):
        if self.userName != user.userName:
            self.notifications.append(f"{user.userName}  commented on your post")
            print("notification to" + self.userName + self.notifications.pop()+": "+comment)

    def StringNotifications(self):
        print(self.userName+"'s notifications:")
        for notification in self.notifications:
            print(notification+"\n")




