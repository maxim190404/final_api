from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
import base64
from django.core.files.base import ContentFile
from posts.models import Comment, Post, Group, Follow, User
from django.shortcuts import get_object_or_404


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(
                base64.b64decode(imgstr),
                name='temp.' + ext)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'created', 'post')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.CharField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        following = get_object_or_404(User, username=data['following'])
        user = self.context['request'].user
        if user == following or Follow.objects.filter(following=following,
                                                      user=user).exists():
            raise serializers.ValidationError("Not Valid")
        return data
