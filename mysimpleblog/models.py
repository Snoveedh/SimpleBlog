from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField


class Post(models.Model):
    
    title = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default="Mysimple Blog!")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank= True, null = True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_post')
    # snippet = models.CharField(max_length=255, default='Click Link Above to read Blog post')
    snippet = models.CharField(max_length=255)  #Here removed the default content, no need to do make migrations if we remove these deaults. first time if u add an object then you need to makemigrations, make migrate
    header_image = models.ImageField(null = True, blank=True, upload_to = "images/")

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

    



class Category(models.Model):

    name  = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank= True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank= True)
    pinterest_url = models.CharField(max_length=255, null=True, blank= True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)





