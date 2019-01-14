from django.test import TestCase

from .models import MyModel, MyModel2


class SampleTestCase(TestCase):
    def test_sample(self):
        obj = MyModel.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample2(self):
        obj = MyModel2.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")
