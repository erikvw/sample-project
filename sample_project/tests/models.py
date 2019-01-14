from django.db import models


class MyModel(models.Model):

    f1 = models.CharField(max_length=25, null=True)


class MyModel2(models.Model):

    f1 = models.CharField(max_length=25, null=True)
