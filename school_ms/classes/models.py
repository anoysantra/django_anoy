from django.db import models

# Create your models here.

class SchoolClasses(models.Model):
    class_name = models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.class_name

