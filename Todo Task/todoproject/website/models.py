from django.db import models

class Record(models.Model):
    title = models.CharField(max_length=150)
    decsription = models.TextField()
    completion = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
