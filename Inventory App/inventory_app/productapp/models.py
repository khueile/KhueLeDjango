from django.db import models

# Create your models here.

class product(models.Model):#ORM established
    title = models.CharField(max_length=55)
    text = models.CharField(max_length=2000)
    create_date = models.DateField()
    publication_date = models.DateField()