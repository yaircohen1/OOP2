from abc import abstractmethod
import matplotlib.pyplot as plt
from PIL import Image as PILImage


class Post:
    def __init__(self, owner):
        self.owner = owner

    #Post have option to get like from others
    def like(self, other_user):
        if other_user.online:
            self.owner.observer.got_like_notification(other_user)

    # Post have option to get comment from others
    def comment(self, other_user, comment_txt):
        if other_user.online:
            self.owner.observer.got_comment_notification(other_user, comment_txt)

    @abstractmethod
    def __str__(self):
        pass
    ##all type of posts need to implements from post and made print on their on way
class PostFactory:
    def create_post(self, user, post_type, *args):
        if post_type == "Text":
            return TextPost(user, *args)
        if post_type == "Image":
            return ImagePost(user, *args)
        if post_type == "Sale":
            return SalePost(user, *args)
        else:
            raise ValueError("Invalid Post type")
# we used *args because post can be one of these options: 1.Text (which get text) 2.image (which get 'image1.jpg')
# 3.Sale (which get product, location, price)

class TextPost(Post):

    def __init__(self, owner, content):
        super().__init__(owner)
        self.content = content
        owner.set_num_of_posts()
        print(self.owner.user_name+" published a post:\n"+'"'+self.content+'"'+"\n")

    def __str__(self):
        return (self.owner.user_name+" published a post:\n"+'"'+self.content+'"'+"\n")


class ImagePost(Post):

    def __init__(self, owner, image_path):
        super().__init__(owner)
        self.image = Image(image_path)
        owner.set_num_of_posts()
        print(f"{self.owner.user_name} posted a picture\n")

    def display(self):
        img = self.image.load_image()
        plt.imshow(img)
        plt.title('Image Post')
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def __str__(self):
        return (self.owner.user_name+" posted a picture\n")

class Image:

    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        # Load the image, and open - using Pillow's Image.open method
        try:
            img = PILImage.open(self.image_path)
            return img

        except Exception as e:
            print(f"Error loading image: {e}")
            return None


class SalePost(Post):

    def __init__(self, owner, product, price, location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.available = True
        owner.set_num_of_posts()
        print(self.owner.user_name + " posted a product for sale:\n" + "For sale! " + self.product + ", price: " + str(
            self.price) + ", pickup from: " + self.location + "\n")

    def sold(self, password):
        if password != self.owner.password:
            raise Exception("Password is wrong")

        if password == self.owner.password and self.available:  # the password is currect and product is available
            self.available = False
            print(self.owner.user_name + "'s product is sold")

    def discount(self, percent, password):
        if password != self.owner.password:
            raise Exception("WRONG PASSWORD, CANNOT MAKE A DISCOUNT")

        if password == self.owner.password and 0 < percent < 100:
            price_after_discount = self.price * (1-percent/100)
            self.price = price_after_discount
            print("Discount on " + self.owner.user_name + " product! the new price is: " + str(self.price))

    def __str__(self):
        if self.available:
                return (self.owner.user_name + " posted a product for sale:\n" + "For sale! " + self.product + ", price: " + str(
            self.price) + ", pickup from: " + self.location + "\n")
        else:
            return (self.owner.user_name + " posted a product for sale:\n" + "Sold! " + self.product + ", price: " + str(
            self.price) + ", pickup from: " + self.location + "\n")
