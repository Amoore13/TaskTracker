from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=128)
    taskId = models.CharField(max_length=128)

    created = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.text
