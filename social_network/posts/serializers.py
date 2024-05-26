from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_at']
        read_only_fields = ['author']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post']
        read_only_fields = ["user"]


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'created_at', 'comments', 'likes']
        read_only_fields = ['user']

    def get_likes(self, obj):
        likes = obj.likes.count()
        return likes