from django.db import models

# Create your models here.

class Position(models.Model):
      title = models.CharField(max_length=100)

      def __str__(self):
            return self.title

class Developer(models.Model):
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      image = models.ImageField(upload_to='image/', blank=True, null=True)
      gender = models.BooleanField(null=True)
      mobile = models.CharField(max_length=15)
      email = models.EmailField(max_length=200)
      position = models.ForeignKey(Position,on_delete=models.CASCADE)
      experience = models.CharField(max_length=100)
      remarks = models.CharField(max_length=200)


  
  