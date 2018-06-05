from django.db import models
from users.models import models, User


# class Status(models.Model):
#     name = models.CharField(max_length=24, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "Статус %s" % self.name
#
#     class Meta:
#         verbose_name = "Статус задачи"
#         verbose_name_plural = "Статусы задачи"


class Task(models.Model):
    name = models.CharField(max_length=128)
    project = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    implementer = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete='CASCADE')
    #user = models.ForeignKey(User, on_delete='CASCADE')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

        def __str__(self):
            return self.text[:50] + "..."
