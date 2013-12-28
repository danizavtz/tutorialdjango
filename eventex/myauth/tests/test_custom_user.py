# coding: utf-8
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import override_settings

@override_settings(AUTH_USER_MODEL='myauth.User')
class FunctionalCustomUserTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        u = UserModel(cpf='12345678901')
        u.set_password('abracadabra')
        u.save()

    def test_login_with_cpf(self):
        self.assertTrue(self.client.login(cpf='12345678901', password='abracadabra'))
