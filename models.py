from django.db import models
    
class Upload(models.Model):
    upload_file = models.FileField(upload_to='documents/')
    
class Ans(models.Model):
    key = models.CharField(max_length=500)
    value = models.CharField(max_length=50)

