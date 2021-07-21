from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import (action, authentication_classes,
                                       permission_classes)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .permissions import IsYAMDBAdministrator
from .serializers import EmailConfirmationSerializer, UserSerializer


def make_random_password(length=10,
                         allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                       'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                       '23456789'):
    return get_random_string(length, allowed_chars)


@action(detail=True, methods=['post', ])
@permission_classes([])
@authentication_classes([])
class EmailConfirmationView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EmailConfirmationSerializer

    @action(detail=False)
    def email(self):
        email = self.request.data['email']
        confirmation_code = make_random_password()
        CustomUser.objects.get_or_create(
            email=email,
            username=email,
            confirmation_code=confirmation_code
        )
        send_mail(
            'confirmation_code',
            f'{confirmation_code}',
            ['user@yandex.ru'],
            fail_silently=False,
        )

    @action(detail=False)
    def token(self):
        email = self.request.POST.get('email')
        if not email:
            return Response({'error': 'email required'},
                            status=status.HTTP_400_BAD_REQUEST)
        confirmation_code = self.request.POST.get('confirmation_code')
        if not confirmation_code:
            return Response({'error': 'confirmation_code required'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(CustomUser, email=email)
        if user.confirmation_code == '':
            return Response({'error': 'confirmation_code expired'},
                            status=status.HTTP_400_BAD_REQUEST)
        if confirmation_code == user.confirmation_code:
            refresh = RefreshToken.for_user(user)
            user.confirmation_code = ''
            user.save()
            data = {'token': str(refresh.access_token)}
            return Response(data, status=status.HTTP_200_OK)
        return Response({'error', 'Wrong confirmation code'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('id', )
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAdminUser | IsYAMDBAdministrator]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(detail=False, methods=['get', 'patch'],
            permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = UserSerializer(user,
                                        data=request.data,
                                        partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return None
