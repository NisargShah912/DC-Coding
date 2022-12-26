from django.db import models

class qrcode(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    extinct = models.CharField(max_length=50)
    img=models.ImageField()
    def __str__(self):
        return self.name

class Signup(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  confpassword = models.CharField(max_length=255)
  def __str__(self):
          return self.name + ' - ' + self.email