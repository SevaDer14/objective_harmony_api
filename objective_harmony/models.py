from django.db import models

class Spectrum(models.Model):
  name = models.CharField(max_length=50)

  def _str_(self):
    return self.name
