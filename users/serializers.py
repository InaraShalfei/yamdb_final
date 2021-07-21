from rest_framework import serializers

from .models import CustomUser


class EmailConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email',)
        model = CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'username', 'first_name',
                  'last_name', 'bio', 'role',)
        model = CustomUser
