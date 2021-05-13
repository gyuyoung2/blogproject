from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    body = models.TextField()