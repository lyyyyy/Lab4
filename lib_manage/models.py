
# Create your models here.
from django.db import models


class Author(models.Model):
    AuthorID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    
class Book(models.Model):
    ISBN = models.AutoField(primary_key = True)
    Title = models.CharField(max_length=30)
    AuthorID  = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.DateField()
    Price = models.CharField(max_length=30)
    
#AuthorID is primary_key in class Author
