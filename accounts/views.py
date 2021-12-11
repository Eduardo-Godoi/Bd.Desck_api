from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer


class CreateUserView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):
        import pdb

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

        # pdb.set_trace()

        return super().get_serializer(*args, **kwargs)


class LoginUserVIew(APIView):

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)

        user = authenticate(**login_serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
