from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=59)
#     email = models.CharField(max_length=59)
#     date_of_birth = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     # followers = models.ManyToManyField(User)
# class Post(models.Model):
#     text = models.CharField(max_length=30)
#     created_at = models.DateField(auto_now_add=True)
#     likes = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Abstract(models.Model):
    text = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(Abstract):
    pass


class Task(Abstract):
    status = models.BooleanField()
    deadline = models.DateField()
    number = models.OneToOneField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Photo(models.Model):
    image = models.ImageField(upload_to='app_10_22/static/images')

# username firstname lastname password email date role


class User(AbstractUser):
    avatar = models.ImageField(upload_to='app_10_22/static/images', default='app_10_22/static/images/default.png')
    status = models.CharField(max_length=100)
