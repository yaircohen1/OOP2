class Post:
    def __init__(self,owner):
        self.owner=owner
    def like(self, user):
        if user.online:
            user.Observer.gotLikeNotification(self.owner.Observer)