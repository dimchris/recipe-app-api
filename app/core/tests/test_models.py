from django.contrib.auth import get_user_model
from django.test.testcases import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user_with_email_successfull(self):

        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_should_fail_with_empty_email(self):

        email = ""
        password = "testpass123"

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_superuser(
                email=email,
                password=password,
            )
