from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Item(models.Model):
	image = CloudinaryField('image')
	name = models.CharField(verbose_name="Item Name", max_length=200, default="")
	description = models.TextField(default='')
	price = models.DecimalField(max_digits=6, decimal_places=2)
