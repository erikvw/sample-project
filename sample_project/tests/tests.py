from django.test import TestCase

from .models import MyModel, MyModel2, MyModel3


class SampleTestCase(TestCase):
    def test_sample(self):
        obj = MyModel.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample2(self):
        obj = MyModel2.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample3(self):
        obj = MyModel3.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample4(self):
        obj = MyModel3.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")
