from rest_framework import serializers
from schoolwebsite.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'all'
