from django.db import models
class user_appointments(models.Model):
    date = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=10, null=True)