from django.db import models

# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField( max_length=250)
    telephone = models.CharField(max_length=14)
    salary = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employe'
        verbose_name_plural = 'Employes'

class Absense(models.Model):
    name = models.ForeignKey(Employe,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    timeIn = models.TimeField(auto_now=True, auto_now_add=False)
    timeOut = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'absense'
        verbose_name_plural = 'absenses'