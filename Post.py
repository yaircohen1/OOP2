from abc import ABC, abstractmethod
from numpy import double
from ex_2 import User
from PIL import Image as PILImage
import matplotlib
import matplotlib.pyplot as plt


class PostFactory(ABC):

            def _creat_post(self, user, post_type: str, *args):
                if post_type == "TextPost":
                    return TextPost(user, *args)
                if post_type == "ImagePost":
                    return ImagePost(user, *args)
                if post_type == "SalePost":
                    return SalePost(user, *args)
                else:
                    raise ValueError("Invalid Post type")


class Post:

    def __init__(self, owner):
        self.owner = owner


    def _new_post(self,user :User):   #All posts have a user who update them
        pass


    def __str__(self):
        pass


    def like(self, other_user):
        if other_user.online:
            self.owner.Observer.gotLikeNotification(other_user)

    def comment(self, other_user, comment_txt):
        if other_user.online:
            self.owner.Observer.gotCommentNotification(other_user, comment_txt)


########################################################################################

class TextPost(Post):

    def __init__(self, owner :User, content :str):
        self.owner = super()._new_post(owner)
        self.content= content
        owner.get_num_of_posts = owner.get_num_of_posts +1
        print(self.owner+" published a post:\n" + self.content)

    def __str__(self):
        print("user "+self.user+", publish a TextPost :"+self.content)



class ImagePost(Post):

    def _new_post(self, owner :User, image_path):
        self.owner = super()._new_post(owner)
        self.image = Image(image_path)
        owner.set_num_of_posts(owner.get_num_of_posts + 1)
        print(self.owner+" posted a picture")

    def _show_image(self):
        img = self.image._load_image()

        if img:
            plt.imshow(img)
            plt.title('Image Post')
            plt.axis('off')
            plt.show()

    def __str__(self):
        print("user "+self.user+"Posted an ImagePost ", self.image_path)


    def __str__(self):
        print("user "+self.user+", publish an ImagePost ." ,"location pic"+self.path)


class Image:

    def __init__(self, image_path):
        self.image_path = image_path

    def _load_image(self):
    # Load the image, and open - using Pillow's Image.open method
        try:
            img = PILImage.open(self.image_path)
            return img

        except Exception as e:
            print(f"Error loading image: {e}")
            return None



class SalePost(Post):

    available = False
    sold = False
    #chang to init
    def __init__(self, owner :User, password, product_decription :str, product_price :double, collection_point : str):
        self.owner = super()._new_post(owner)
        self.product_price = product_price
        self.collection_point = collection_point
        self.password = password
        self.available = True                         #initilize to be true
        self.sold = False
        owner.get_num_of_posts = owner.get_num_of_posts + 1
        print(self.owner + " posted a product for sale: \n" +
              self.product_decription +", price: "+self.product_price+" pickup from: "+self.collection_point )


    def is_available(self):
        return self.available


    def is_sold(self, password , is_sold :bool):
        if password != self.password:
             print("WRONG PASSWORD, CANNOT SOLD THE PRODUCT")
            #consider do a loop for 3 trys

        if password == self.password and is_sold:    #the password is currect
            self.sold = True


    def discount(self, password, percent:double ):    #the input percent is get as a o.xxx

        if password != self.password:
            print("WRONG PASSWORD, CANNOT MAKE A DISCOUNT")

         #consider if percent < 0 or percent > 1
        if password == self.password and 0< percent <1:
            price_after_discount = percent*(self.product_price/100)
            self.product_price = price_after_discount


    def __str__(self):
        if self.sold:
            print("user "+self.user+", publish a SalePost - the product is available ." 
                                "\n product details "+self.product_decription+".\n product_price : "+self.product_price+".\n collection point :"+self.collection_point)

        else:  # the product is been sold
            print("user "+self.user+", publish a SalePost - the product is sold ." 
                                "\n product details "+self.product_decription+".\n product_price : "+self.product_price+".\n collection point :"+self.collection_point)


