from django.db import models

# Create your models here.
from accounts.models import User

class Lead(models.Model):

    STATUS_CHOICES =[
        ("new","new"),
        ("Contacted","Contacted"),
        ("Interested","Interested"),
        ("Converted","Converted"),
        ("Lost","Lost"),
    ]

    SOURCE_CHOICES = [
        ("Website","Website"),
        ("Social Media","Social Media"),
        ("Referral","Referral"),
        ("Advertisement","Advertisement"),
        ("Other","Other"),
    ]

    name = models.CharField(max_length=30)

    email = models.EmailField()

    phone = models.CharField(max_length=12)

    company = models.CharField(max_length=200,blank=True,null=True)

    source = models.CharField(max_length=200,choices=SOURCE_CHOICES)

    status = models.CharField(max_length=200,choices=STATUS_CHOICES,default="new")

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="leads")




