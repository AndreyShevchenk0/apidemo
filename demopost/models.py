from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
User = get_user_model()


class Post(models.Model):
    """ Модель Отправки """
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    added_post = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250,)
    liked = models.IntegerField(default=0)
    anliked = models.IntegerField(default=0)
    update_post = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.pk)



# class User(AbstractBaseUser, PermissionsMixin):
#     post = models.ForeignKey(Post, related_name="users", on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=25, unique=True)
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=140)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = "username"
#
#     def __str__(self):
#         return self.is_active




