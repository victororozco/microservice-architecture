"""
Profile App Serializers
"""
import re
import uuid
import warnings

from django.conf import settings
from rest_auth.utils import import_callable
from django.contrib.auth import get_user_model
from datetime import datetime

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field

from allauth.account.admin import EmailAddress
from django.contrib.auth.forms import PasswordResetForm

#Override Registartion library

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.utils.translation import ugettext as _

from rest_framework import serializers, fields

from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

from profiles.models import (
    User
)

from profiles.serializers import (
    UserProfileSerializer
)

class LoginSerializer(RestAuthLoginSerializer):
    username = None

class JWTSerializer(serializers.Serializer):
    """
    Serializer for JWT authentication.
    """
    token = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
        JWTUserDetailsSerializer = import_callable(
            rest_auth_serializers.get('USER_DETAILS_SERIALIZER', UserProfileSerializer)
        )
        user_data = JWTUserDetailsSerializer(obj['user'], context=self.context).data
        return user_data

def jwt_response_payload_handler(token, user=None, request=None):

    data = UserProfileSerializer(user, context={'request': request}).data

    return {
        'success': True,
        'token': token,
        'user': UserProfileSerializer(user, context={'request': request}).data
    }

def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'username': username,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if hasattr(user, 'dni'):
        payload['dni'] = user.dni
    if hasattr(user, 'first_name'):
        payload['first_name'] = user.first_name
    if hasattr(user, 'last_name'):
        payload['last_name'] = user.last_name
    if hasattr(user, 'role'):
        payload['role'] = user.role
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload