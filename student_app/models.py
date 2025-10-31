from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=40)
    last_name  = models.CharField(max_length=40)
    files = models.CharField(max_length=40)
    aboat = models.CharField(max_length=255)
    work = models.BooleanField(default=False)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name