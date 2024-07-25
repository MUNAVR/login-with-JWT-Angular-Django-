from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_image']  # Add other fields if needed

