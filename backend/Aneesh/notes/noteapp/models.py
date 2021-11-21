from django.db import models

# Create your models here.
class Notes(models.Model):
    NoteId= models.AutoField(primary_key=True)
    NoteCont= models.CharField(max_length=1000)






    
