from django.db import models
from django.utils import timezone

# Create your models here.
class activities(models.Model):
    event = models.CharField(max_length=300)
    type=models.CharField( max_length=20)
    result=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    event_date = models.DateTimeField("date logged")
'''
    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.event_date)
        return f"'{self.event}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
# Create your models here.
'''