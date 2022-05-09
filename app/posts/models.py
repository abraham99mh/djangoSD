from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    price = models.EmailField()
    user_id = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
