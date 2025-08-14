
from django.db import models
import string, random

def generate_shortcode():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URL(models.Model):
    original_url = models.URLField()
    shortcode = models.CharField(max_length=6, unique=True, default=generate_shortcode)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shortcode} → {self.original_url}"


# Create your models here.
