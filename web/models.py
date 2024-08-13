from django.db import models
import uuid

class Flan(models.Model):
  flan_uuid = models.UUIDField(default=uuid.uuid4)
  name = models.CharField(max_length=50)
  description = models.TextField()
  image_url = models.URLField()
  slug = models.SlugField()
  is_private = models.BooleanField()
  
  def __str__(self):
    return f"{self.name}:{self.is_private}"