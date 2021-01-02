from django.test import TestCase
from apple.models import person,order


class person_order_test(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user1 = person.objects.create(first_name='sidhu',last_name='sahoo',
                                          age=21, ph_no=738839494 )
        cls.order = order.objects.create(person=cls.user1,item='food')
        cls.order = order.objects.create(person=cls.user1,item='food')
    def test_person(self):

        self.assertEqual(str(self.user1.first_name),'sidhu')
        self.assertEqual(self.user1.ph_no,738839494)


    def test_order(self):
        self.assertEqual(order.objects.count(),2)


