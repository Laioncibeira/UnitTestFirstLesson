from django.test import TestCase
from UnitTesting import email


class TestEmail(TestCase):
    def test_is_mail_successfully(self):
        """los test tienen 3 AAA:
        Arrange: declaración de todo lo que necesito para testear (objetos, variables, etc)"""
        mail = "hulala@gmail.com"
        """Act: Ejecutar el metodo que quiero testear"""
        result = email.is_mail(mail)
        """Assert: Comparas el resultado del metodo con lo que vos esperas que devuelva el met testeado"""
        self.assertEqual(result, True)

    def test_is_mail_fail(self):
        #Arrange:
        mail = "hulala@gmail.con"
        #Act:
        result = email.is_mail(mail)
        #Assert:
        self.assertEqual(result, False)
