from django.db import models

# Create your models here.
class Post(models.Model):
  titolo = models.CharField(max_length=200)
  descrizione = models.TextField()
  data_creazione = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titolo
