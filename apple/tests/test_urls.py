from django.test import SimpleTestCase
from django.urls import reverse,resolve
from apple import  views


class Test_urls(SimpleTestCase):

    def test_to_urls(self):

        url = reverse('index')
        # print(resolve(url))
        self.assertEqual(resolve(url).func,views.index)



