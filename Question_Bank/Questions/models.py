from django.db import models

# Create your models here.
class question(models.Model):
    text = models.CharField(max_length = 2000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    correct = models.CharField(max_length = 1)
    subject = models.IntegerField(null=True)
    week = models.IntegerField(null = True)
    topic = models.CharField(max_length = 500, null = True)
