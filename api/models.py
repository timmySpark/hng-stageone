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


class arit(models.Model):
    oper=(
        ('Addition', '+'),
        ('Subtraction', '-'),
        ('Division', '/'),
    )
    operation_type = models.CharField(max_length=100, choices=oper, default='Addition')
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        verbose_name =("Arit")
        verbose_name_plural =("Arit")