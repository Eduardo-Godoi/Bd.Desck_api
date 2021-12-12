from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer


class CreateUserView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):

        zip_code = self.request.data.get('zip_code', None)
        public_area = self.request.data.get('public_area', None)
        number = self.request.data.get('number', None)
        district = self.request.data.get('district', None)
        city = self.request.data.get('city', None)
        state = self.request.data.get('state', None)

        self.request.data['address'] = {
            'zip_code': zip_code,
            'public_area': public_area,
            'number': number,
            'district': district,
            'city': city,
            'state': state
        }

        return super().get_serializer(*args, **kwargs)


class LoginUserVIew(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        user = authenticate(**request.data)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
