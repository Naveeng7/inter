from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class items(models.Model):
    title = models.CharField(max_length=75)
    img = models.ImageField(default='default.jpg', upload_to='itempic')
    desc = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(items, self).save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.img.path)

