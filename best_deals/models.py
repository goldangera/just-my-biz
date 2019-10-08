from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.CharField(max_length=100,default=None)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
    @classmethod
    def search_by_category(cls,search_term):
        businesses = cls.objects.filter(categories__icontains=search_term)
        return businesses
