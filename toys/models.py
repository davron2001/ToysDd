from django.db import models

class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

class User(models.Model):
    is_active = models.BooleanField(default=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.OneToOneField(Address,on_delete=models.PROTECT, null=True, blank=True)

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="toys",on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="toys")

