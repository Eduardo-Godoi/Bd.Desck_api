from accounts.models import Address, User
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'nilton'
        cls.full_name = 'Nilton Santos'
        cls.email = 'nilton@mail.com'
        cls.password = '11nilton00'

        cls.zip_code = '78559649'
        cls.public_area = 'Rua Dois'
        cls.number = 'B3'
        cls.district = 'Boa Vista'
        cls.city = 'Sinop'
        cls.state = 'MT'

        cls.address = Address.objects.create(
            zip_code=cls.zip_code,
            public_area=cls.public_area,
            number=cls.number,
            district=cls.district,
            city=cls.city,
            state=cls.state
        )
        
        cls.user = User.objects.create_user(
            username=cls.username,
            full_name=cls.full_name,
            email=cls.email,
            password=cls.password,
            address_id=cls.address.id
        )

    def test_address_fields(self):

        self.assertIsInstance(self.address.zip_code, str)
        self.assertEqual(self.address.zip_code, self.zip_code)

        self.assertIsInstance(self.address.public_area, str)
        self.assertEqual(self.address.public_area, self.public_area)

        self.assertIsInstance(self.address.number, str)
        self.assertEqual(self.address.number, self.number)

        self.assertIsInstance(self.address.district, str)
        self.assertEqual(self.address.district, self.district)

        self.assertIsInstance(self.address.city, str)
        self.assertEqual(self.address.city, self.city)

        self.assertIsInstance(self.address.state, str)
        self.assertEqual(self.address.state, self.state)




    def test_user_fields(self):

        self.assertIsInstance(self.user.full_name, str)
        self.assertEqual(self.user.full_name, self.full_name)

        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, self.email)

        self.assertIsInstance(self.user.password, str)

        self.assertEqual(self.address, self.user.address)

