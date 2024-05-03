from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_at']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'created_at']
        read_only_fields = ['user']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'likes_count', 'post']
        read_only_fields = ["user"]


class FullPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id','user', 'text', 'image', 'created_at', 'comments', 'likes']
        read_only_fields = ['user']

    def get_likes(self, obj):
        print(obj.id)
        likes_count = Like.objects.all().filter(post_id=obj.id).values("likes_count").count()
        return likes_count