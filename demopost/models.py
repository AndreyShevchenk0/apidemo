from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    """ Модель Отправки """
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    title = models.TextField(unique=True)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    liked = models.IntegerField(default=0)
    unliked = models.IntegerField(default=0)


# class tUser(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     """
#     email = models.EmailField(max_length=40, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#         return self