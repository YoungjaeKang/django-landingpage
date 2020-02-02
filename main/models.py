from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dataCreate = models.DateTimeField()
    category = models.TextField()

    def __str__(self):
        return self.title