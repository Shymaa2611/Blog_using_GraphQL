from rest_framework import serializers
from .models import Author,Post

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        
