from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class PostsUserWritePermission(BasePermission):
    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        # Check permissions for read-only requestelse:
        if request.method in SAFE_METHODS:
            return True

         # Check permissions for write request
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobject.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostsUserWritePermission):
    permission_classes = [PostsUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
