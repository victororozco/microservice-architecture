"""
Profiles app views
"""
from datetime import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_auth.serializers import PasswordChangeSerializer, PasswordResetConfirmSerializer
from allauth.account.admin import EmailAddress
from rest_auth.registration.views import RegisterView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken, JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from django.contrib.auth.signals import user_logged_in

from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)
from rest_framework import (
    status, generics, mixins, permissions, viewsets, filters
)

from rest_auth.serializers import (
            LoginSerializer, JWTSerializer
)

from rest_auth.models import(
    TokenModel
)

from allauth.account.adapter import get_adapter

from rest_auth.utils import jwt_encode

from rest_framework.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator

from django.http import JsonResponse, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from profiles.models import (
    User
)

from profiles.serializers import (
    UserProfileSerializer
)

from .serializers import (
    JWTSerializer,
    UserProfileSerializer,
    jwt_response_payload_handler,
    jwt_payload_handler
)

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.contrib.auth.__init__ import get_user_model

UserModel = get_user_model()

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)

class CustomLoginView(APIView):
    """
    Base API View that various JWT interactions inherit from.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = JSONWebTokenSerializer

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'view': self,
        }

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__)
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            try:
                user_logged_in.send(sender=user.__class__, request=request, user=user)
            except Exception as e:
                print(e)
            response = Response(response_data)
            # if api_settings.JWT_AUTH_COOKIE:
            #     expiration = (datetime.utcnow() +
            #                   api_settings.JWT_EXPIRATION_DELTA)
            #     response.set_cookie(api_settings.JWT_AUTH_COOKIE,
            #                         token,
            #                         expires=expiration,
            #                         httponly=True)
            return response
        data_error = {
            'success': False,
            'detail' : "Usuario o contraseña inválido"
            }
        return JsonResponse(data_error, status=status.HTTP_400_BAD_REQUEST)

class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer
