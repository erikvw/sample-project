from django.db import models


class MyTestModel1(models.Model):

    f1 = models.CharField(max_length=25, null=True)


class MyTestModel2(models.Model):

    f1 = models.CharField(max_length=25, null=True)
