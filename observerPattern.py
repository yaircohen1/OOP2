class UserObservable:
    # userObservable is observable, and when updates about the user are updated, the state of userObservable changes.
    def __init__(self, user_name):
        self.observers = []  # all the observers (followers) that get updates from this userObservable
        self.user_name = user_name

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            print(observer.user_name + " started following " + self.user_name)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            print(observer.user_name + " unfollowed " + self.user_name)

    def num_followers(self):
        return self.observers.__sizeof__()


class Observer:
    # followers
    def __init__(self, user_name):
        self.user_name = user_name
        self.notifications = []  # all the notifications the user got

    def got_like_notification(self, user):
        if self.user_name != user.user_name:
            self.notifications.append(f"{user.user_name} liked your post")
            print("notification to" + self.user_name + self.notifications.pop())

    def got_comment_notification(self, user, comment):
        if self.user_name != user.user_name:
            self.notifications.append(f"{user.user_name}  commented on your post")
            print("notification to" + self.user_name + self.notifications.pop() + ": " + comment)

    def got_friend_upload_post(self,):
    def print_o_notifications(self):
        print(self.user_name + "'s notifications:")
        for notification in self.notifications:
            print(notification + "\n")
