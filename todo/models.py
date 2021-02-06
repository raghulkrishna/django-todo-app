from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    deleted =  models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prio = (('H','High'),('M','Medium'),('L','Low'))
    priority = models.CharField(max_length=1, choices=prio)

    def __str__(self):
        return self.title