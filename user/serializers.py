from rest_framework import serializers

from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def update(self, validated_data):
        user = User.objects.update(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_img', 'about_me']

    def create(self, validated_data):
        user = self.request.user
        profile = Profile.objects.create(
            user=user,
            nickname=validated_data['nickname'],
            img=validated_data['profile_img'],
            about=validated_data['about_me']
        )
        return profile


