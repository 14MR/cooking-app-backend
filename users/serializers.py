from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
