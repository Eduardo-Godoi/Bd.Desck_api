from accounts.models import Address, User
from rest_framework.test import APITestCase


class UserViewTest(APITestCase):

    def test_create_new_user(self):
        user_data = {
            "full_name": "Nilton Santos",
            "email": "test@mail.com",
            "password": "test1221",
            "username": "nill12",
            "zip_code": "78559649",
            "public_area": "Rua Dois",
            "number": "B3",
            "district": "Boa Vista",
            "city": "Sinop",
            "state": "MT"
        }

        response = self.client.post("/api/accounts/", user_data, format='json')

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.json()['full_name'], "Nilton Santos")
        self.assertNotIn('password', response.json())


    def test_create_user_fail(self):
        user_data = {
            "username": "nill12",
            "zip_code": "78559649",
            "public_area": "Rua Dois",
            "number": "B3",
            "district": "Boa Vista",
            "city": "Sinop",
            "state": "MT"
        }

        response = self.client.post("/api/accounts/", user_data, format='json')

        self.assertEqual(response.status_code, 400)


class LoginViewTest(APITestCase):
    def setUp(self):

        address = Address.objects.create(
            zip_code="78559649",
            public_area="Rua Dois",
            number="B3",
            district="Boa Vista",
            city="Sinop",
            state="MT"
        )

        User.objects.create_user(
            full_name="Nilton Santos",
            email="test@mail.com",
            password="test1221",
            username="nill12",
            address_id=address.id
        )

    def test_login_success(self):
        login_data = {
            'username': 'nill12',
            'password': 'test1221',
        }

        response = self.client.post('/api/login/', login_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())

    def test_login_invalid_password(self):
        login_data = {
            'username': 'nill12',
            'password': '12'
        }

        response = self.client.post('/api/accounts/', login_data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_login_missing_fields(self):
        login_data = {
            'password': 'test1221'
        }

        response = self.client.post('/api/accounts/', login_data, format='json')

        self.assertEqual(response.status_code, 400)
