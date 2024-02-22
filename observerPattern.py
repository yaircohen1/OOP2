class UserObservable:
    # userObservable is observable, and when updates about the user (follow, remove follow or upload post) the observers (followers) get update
    def __init__(self, user_name):
        self.observers = []  # all the observers (followers) that get updates from this userObservable
        self.user_name = user_name

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer) #add them to followers list
            print(observer.user_name + " started following " + self.user_name)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer) #remove them from followers list
            print(observer.user_name + " unfollowed " + self.user_name)

    def upload_post(self):
        for observer in self.observers:
            observer.notifications.append(f"{self.user_name} has a new post") #followers got update that user upload post

    def num_followers(self):
        return len(self.observers)


class Observer:
    # followers
    def __init__(self, user_name):
        self.user_name = user_name
        self.notifications = []  # all the notifications the user get

    #got update that user like your post
    def got_like_notification(self, user):
        if self.user_name != user.user_name:
            notification =f"{user.user_name} liked your post"
            self.notifications.append(notification)
            print("notification to " + self.user_name +": " +notification)

    # got update that user comment on your post
    def got_comment_notification(self, user, comment):
        if self.user_name != user.user_name:
            notification =f"{user.user_name} commented on your post"
            self.notifications.append(notification)
            print("notification to " + self.user_name +": "+notification + ": " + comment)

    def print_o_notifications(self):
        print(self.user_name + "'s notifications:")
        for notification in self.notifications:
            print(notification)
