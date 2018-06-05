from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    project = models.CharField(max_length=128)
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.name
