from django.db import models

# Create your models here.
class text (models.Model) :
    te = models.CharField(max_length=200)

    def __str__(self):
        if len(self.te) < 50:
            return self.te 
        return f"{self.te[:50]}..."