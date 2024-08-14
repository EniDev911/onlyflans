from django.db import models
import uuid
from django.utils.text import slugify

class Flan(models.Model):
  flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  description = models.TextField()
  image_url = models.URLField()
  slug = models.SlugField(max_length=200, unique=True, blank=True)
  is_private = models.BooleanField()
  
  def save(self, *args, **kwargs):
    if not self.slug.strip():
      self.slug = slugify(self.name)
    super(Flan, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.name}:{self.is_private}"

class ContactForm(models.Model):
  contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  contact_form_email = models.EmailField(max_length=100)
  contact_form_name = models.CharField(max_length=64)
  message = models.TextField()