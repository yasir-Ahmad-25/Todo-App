from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    due_date = models.DateField(blank=True , null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="tasks" , null=True)
    

    # return string instead of class
    def __str__(self):
        return self.title
    