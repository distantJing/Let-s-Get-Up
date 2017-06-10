from django.db import models

# Create your models here.
class MemberInfo(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.
