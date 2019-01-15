from django.db import models


class MyModel(models.Model):

    f1 = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.f1
