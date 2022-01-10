from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField(blank=True,null=True,default='pw4.jpg.url')
    follows = models.ManyToManyField(User,related_name="followers",blank=True)

    @classmethod
    def get_follows(cls,users):
            profiles_list = []
            for user in users:
                profiles = Profile.objects.filter(user = user)
                for profile in profiles:
                    profiles_list.append(profile)

            return profiles_list
    @classmethod
    def follow_profile(self,user):
            """This will add a user as a liker of an image
            """
            self.follows.add(user)

    def get_follows_total(self):
            """This will return the number of likes of a particular post
            """
            return self.follows.count()


class Picture(models.Model):
    user = ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = CloudinaryField(blank=True)
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(User,related_name="likers",blank=True)
    post_date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return self.description

    def save_picutre(self):
        self.save()


    def get_picture_by_id(id):
        picture = Picture.objects.get(pk=id)
        return picture

    def save_picture(self):
         self.save()

    def delete_picture(self):
        """This deletes the image from the database using its pk
        Args:
            id ([type]): [description]
        """
        self.delete()
    
    def update_picture(self,new):
        """This method will update a record of an image
        """
        
        self.image = new.image
        self.description = new.description
        self.post_date = new.post_date
        self.likes = new.likes
        self.save()

    @classmethod
    def get_images(cls,users):
        posts = []
        for user in users:
            pictures = Picture.objects.filter(user = user)
            for picture in pictures:
                posts.append(picture)

        return posts
    @classmethod
    def get_comments(self):
        """This will return all the comments related to a post
        Returns:
            [type]: [description]
        """
        comments = Comments.objects.filter(image = self)
        return comments

    def like_image(self,user):
        """This will add a user as a liker of an image
        """
        self.likes.add(user)

    def get_likes_total(self):
        """This will return the number of likes of a particular post
        """
        return self.likes.count()


    


class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Picture,on_delete=models.CASCADE,null=True)
    comment = TextField(blank=True)

    def save_comment(self):
        """
        This adds a category to the database
        """
        self.save()

    def delete_comment(self):
        """
        This removes a category from the database
        """
        self.delete()

    def update_comment(self,new):
        """This will update a category
        Args:
            new ([type]): [description]
        """
        self.name = new.description
        self.save()

    def __str__(self):
        return self.name

    