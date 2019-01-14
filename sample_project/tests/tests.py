from django.test import TestCase

from .models import MyModel


class SampleTestCase(TestCase):
    def test_sample(self):
        obj = MyModel.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")
