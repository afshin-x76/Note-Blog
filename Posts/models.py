from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    age_numbers = list(range(10, 80))
    age_list = list()
    for i in age_numbers:
        age_list.append((str(i), str(i)))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
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


class Post(models.Model):
    title = models.CharField(max_length=25)
    thumbnail = models.ImageField()
    overview = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


