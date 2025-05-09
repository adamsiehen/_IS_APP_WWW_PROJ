from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)


class Topic(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
 #Lab5 - przeciązanie operatorów
 #Lab6 - zmodyfikowanie widoku
    def __str__(self):
        return f"Topic : {self.name}, dodany {self.created}, w kategorii {self.category.name}." 
    
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False),
    modified_at = models.DateTimeField(auto_now=True, editable=False),
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#Lab5      
    def __str__(self):
        return self.content[:20] + "..."
    