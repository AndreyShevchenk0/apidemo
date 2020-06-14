from rest_framework import serializers
from demopost.models import Post


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'  # виводить все поля


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

#     class Meta(object):
#         model = Post  # Разработать модель
#         fields = ('id', 'email', 'first_name', 'last_name',
#                   'date_joined', 'password')
#         extra_kwargs = {'password': {'write_only': True}}