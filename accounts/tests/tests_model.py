from accounts.models import User
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'nilton@mail.com'
        cls.full_name = 'Nilton Santos'
        cls.email = 'nilton@mail.com'
        cls.password = '11nilton00'

        cls.user = User.objects.create_user(
            username='nilton@mail.com',
            full_name=cls.full_name,
            email=cls.email,
            password=cls.password
        )

    def test_user_fields(self):

        self.assertIsInstance(self.user.full_name, str)
        self.assertEqual(self.user.full_name, self.full_name)

        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, self.email)

        self.assertIsInstance(self.user.password, str)

