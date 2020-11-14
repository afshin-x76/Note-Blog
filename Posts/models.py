from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Subscribes(models.Model):
    user = models.ForeignKey(User,related_name="user", on_delete=models.CASCADE)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


class Author(models.Model):
    age_numbers = list(range(10, 80))
    age_list = list()
    for i in age_numbers:
        age_list.append((str(i), str(i)))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)
    age = models.CharField(
        choices=age_list,
        default="25",
        max_length=2)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    write_in = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default="")
    post = models.ForeignKey('Post', related_name='comments' , on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class View(models.Model):
    post = models.ForeignKey('Post', related_name='views', on_delete=models.CASCADE)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=25)
    thumbnail = models.ImageField()
    overview = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs = {'id':self.pk})

    @property
    def comment_count(self):
        return self.comments.all().count()

    def view_count(self):
        return self.views.all().count()



    




