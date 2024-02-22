from observerPattern import *
from Post import *

class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.observer = Observer(self.user_name)
        self.user_observable = UserObservable(self.user_name)
        self.password = password
        self.online = True
        self.num_of_posts = 0

    def get_num_of_posts(self):
        return self.num_of_posts

    def set_num_of_posts(self, num):
        self.num_of_posts = num

    def follow(self, other_user):
        if self.online:
            other_user.UserObservable.attach(self.observer)
            # user enters to the observers (followers) list of
            # otherUser

    def unfollow(self, other_user):
        if self.online:
            other_user.UserObservable.remove(self.observer)  # user left the observers (followers) list of otherUser

    def publish_post(self, type_post, *args):
        post_factory = PostFactory()
        new_post = post_factory.create_post(self, type, *args)
        self.__posts.append(new_post)
        return new_post

    def print_notifications(self):
        self.observer.print_o_notifications()

    def __str__(self):
        return (f"User name:{self.user_name}, Number of Posts:{self.get_num_of_posts()}, "
                f"Number of followers:{self.user_observable.num_followers()}")
