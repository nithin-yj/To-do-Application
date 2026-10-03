from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering=['status']
    
