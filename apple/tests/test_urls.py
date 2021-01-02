from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse,resolve
from apple import  views


class Test_urls(SimpleTestCase):

    def test_to_urls(self):

        url = reverse('index')
        # print(resolve(url))
        self.assertEqual(resolve(url).func,views.index)



class Urltest(TestCase):

    def test_home_url(self):

        responce = self.client.get('/')
        self.assertEqual(responce.status_code,200)


