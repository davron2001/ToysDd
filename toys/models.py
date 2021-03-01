from django.db import models

class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class User(models.Model):
    is_active = models.BooleanField(default=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()

    objects = models.Manager
    active_objects = ActiveObjectsManager()

class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="toys",on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
