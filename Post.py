class Post:
    def __init__(self, owner):
        self.owner = owner

    def like(self, other_user):
        if other_user.online:
            self.owner.Observer.gotLikeNotification(other_user)

    def comment(self, other_user, comment_txt):
        if other_user.online:
            self.owner.Observer.gotCommentNotification(other_user, comment_txt)
