from django.db import models
from base_user.models import MyUser
User=MyUser

# Create your models here.
class Key(models.Model):
    choices = (('SSH', ("SSH")),
               ('FTB', ("FTB")),
               ('ADMIN', ("ADMIN")),
               ('EMAIL', ("EMAIL")))

    type=models.CharField(max_length=255,choices=choices,default=choices[2][0])
    host=models.CharField(max_length=12)
    port=models.GenericIPAddressField(null=True,blank=True)
    user=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user},{self.type}'