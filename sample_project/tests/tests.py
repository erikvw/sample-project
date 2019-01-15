from django.test import TestCase

from ..models import MyModel

from .models import MyTestModel1, MyTestModel2


class SampleTestCase(TestCase):
    def test_sample(self):
        obj = MyModel.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample2(self):
        obj = MyTestModel1.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")

    def test_sample3(self):
        obj = MyTestModel2.objects.create(f1="erik")
        self.assertEqual(obj.f1, "erik")
