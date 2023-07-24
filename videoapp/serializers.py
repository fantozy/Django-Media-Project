from rest_framework import serializers
from .models import Comment, Like, Video, Dislike
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['user', 'body', 'video']

    def get_user(self,obj):
        return obj.user.username
    
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Like
        fields = ['user', 'video']  

    def get_user(self,obj):
        return obj.user.username

class DislikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Dislike
        fields = ['user', 'video']
        
    def get_user(self, obj):
        return obj.user.username