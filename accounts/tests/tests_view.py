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
