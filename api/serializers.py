from blog.models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author', 'content', 'created_on', 'updated_on')