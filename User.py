from observerPattern import *
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

    def set_num_of_posts(self):
        self.num_of_posts = self.num_of_posts+1

    def follow(self, other_user):
        other_user.user_observable.attach(self.observer) #user has been added to observers (followers) list of otherUser

    def unfollow(self, other_user):
        if self.online:
            other_user.user_observable.remove(self.observer)  # user left the observers (followers) list of otherUser

    def publish_post(self, type_post, *args):
        from Post import PostFactory
        if self.online:
            post_factory = PostFactory() #we used factory design
            new_post = post_factory.create_post(self, type_post, *args) #we create new post with post factory design
            self.user_observable.upload_post() #update all the observers (followers) that user publish post
            return new_post

    def print_notifications(self):
        self.observer.print_o_notifications()

    def __str__(self):
        return (f"User name: {self.user_name}, Number of posts: {self.get_num_of_posts()}, "
                f"Number of followers: {self.user_observable.num_followers()}")
