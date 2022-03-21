from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Member(models.Model):
    PLANS = (('Diamond','Diamond'),('Gold','Gold'),('Silver','Silver'))
    user = models.OneToOneField(User,null = True,on_delete = models.CASCADE,default=True)
    name  = models.CharField(null=True,max_length=200)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
    plans = models.CharField(max_length=200,choices=PLANS,default= 'PLANS[0]')
    profile_pic = models.ImageField(default="/Koala.jpg/")
    email_request = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)




    # def get_absolute_url(self):
    #     return reverse('customer')    #,kwargs={"uidb64": self.get_decode()})
    
    
class picture_clergy(models.Model):
    image = models.ImageField(default="/Koala.jpg/")
    text = models.TextField(null=True)
    name = models.CharField(null=True, max_length=200)

    def __str__(self):
        return str(self.image)