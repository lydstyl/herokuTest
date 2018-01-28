from django.db import models

class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #Timespamted hérite de Model et est une classe abstraite qu'on ne peut pas instancier

# Create your models here.
class Post(TimespamtedModel): # du coup ça hérite de Model et de TimespantedModel
    title = models.CharField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return self.title # plus jolie quand on fait from blog.models import Post puis Post.objects.all()