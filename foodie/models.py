from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class items(models.Model):
    title = models.CharField(max_length=75)
    img = models.ImageField(default='default.jpg', upload_to='itempic')
    desc = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)

