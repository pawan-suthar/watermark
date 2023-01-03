from django.db import models
import uuid

# Create your models here.
class ImageModel(models.Model):
    uid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to="images")
    water_mark = models.CharField(max_length=100)
