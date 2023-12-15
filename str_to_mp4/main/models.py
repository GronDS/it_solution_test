from django.db import models
from datetime import datetime    


class Videos(models.Model):
    word = models.TextField('Request')
    date = models.DateTimeField('Request time', default=datetime.now)
    
    def __str__(self) -> str:
        return self.word
    
    class Meta:
        verbose_name = "Videos" 
        verbose_name_plural = "video"