from django.db import models
import uuid
# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email
    
class Notes(models.Model):
    email = models.CharField(max_length=255)
    title = models.TextField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email
