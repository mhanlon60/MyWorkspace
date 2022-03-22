from django.db import models


# Username = MarkH
# Password = Password

class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    startdate = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
