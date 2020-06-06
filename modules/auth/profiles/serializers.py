"""
Profile App Serializers
"""
from rest_framework import serializers, fields

from profiles.models import (
    User
)

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Person-Profile model serializaer
    """

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'dni',
            'role'
        )