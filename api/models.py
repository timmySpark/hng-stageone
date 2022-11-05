from django.db import models

# Create your models here.

class Bio(models.Model):
    slackUsername = models.CharField(max_length=50)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=100)
    

    class Meta:
        verbose_name =("Bio")
        verbose_name_plural =("Bios")

    def __str__(self):
        return self.slackUsername


class Solve(models.Model):
    operation_type = models.CharField(max_length=100, )
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        verbose_name =("Solve")
        verbose_name_plural =("Solve")
        
    def __str__(self):
        return self.operation_type    