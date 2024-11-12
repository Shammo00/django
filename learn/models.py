from django.db import models

# Create your models here.
class text (models.Model) :
    te = models.CharField(max_length=200)

    def __str__(self):
        if len(self.te) < 50:
            return self.te 
        return f"{self.te[:50]}..."
    
class Topic (models.Model) :
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Entry (models.Model) :
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")
