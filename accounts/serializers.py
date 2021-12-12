from rest_framework import serializers

from accounts.models import Address, User


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'username', 'address', 'password']

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True
            }
        }

    def create(self, validate_data):
        address_serialized = AddressSerializer(data=validate_data.pop('address'))
        address_serialized.is_valid(raise_exception=True)
        address = address_serialized.save()

        return User.objects.create_user(**validate_data, address=address)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
