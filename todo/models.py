from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    due_date = models.DateField(auto_now=True)

    # return string instead of class
    def __str__(self):
        return self.title
    