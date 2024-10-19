from django.db import models

# Create your models here.
from django.db import models  
class Crud(models.Model):  
    name = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    contact = models.IntegerField()  
    dob=models.DateField()
    class Meta:  
        db_table = "Crud"  
    def __str__(self):
        return f'Name : {self.name}'