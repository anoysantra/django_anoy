from django.db import models
from django.db import models
from classes.models import SchoolClasses  


class Section_class(models.Model):
    section_name = models.CharField(max_length=1)  
    #class_name = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)
    class_name = models.ManyToManyField(SchoolClasses,max_length=10)

    def __str__(self):
        return f"{self.class_name} - Section {self.section_name}"




