from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=20)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

    def register(self):
        self.save()