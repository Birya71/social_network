from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer, FullPostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # print(type(self.request.user))
        serializer.save(user=self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FullPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    #authentication_classes = [TokenAuthentication]
    serializer_class = FullPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

