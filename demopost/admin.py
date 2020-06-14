from django.contrib import admin
from django.conf import settings
from .models import Post


admin.site.register(Post)
