from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

from django.db import models
from tinymce.models import HTMLField

User =get_user_model()

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title  = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name='previouspost', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='nextpost', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'title': self.title 
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    


'''
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
'''

class Comment(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        #return self.user.username
        return 'Comment {} by {}'.format(self.body, self.name)


class Gallery(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
