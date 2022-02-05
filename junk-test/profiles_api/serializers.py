from rest_framework import serializers

from profiles_api import models



class HelloSerializer(serializers.Serializer):
    """seriliazes a name field for testing out api view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile obj"""

    class Meta:
        model = models.UserProfile
        #making an exception in password field
        fields = ('id', 'email','name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializes profiles feed ProfileFeedItem"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
