from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Post
from api.serializers import PostSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer