from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phong(models.Model):
    Ten = models.CharField(max_length=200, null=True)
    Gia4tieng = models.FloatField(null=True)
    Gia20h_9h = models.FloatField(null=True)
    Gia1h_19h = models.FloatField(null=True)
    Gia14h_12h = models.FloatField(null=True)
    Diachi = models.CharField(max_length=200, null=True)
    Netflix = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Beprieng = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Bontam = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    Diachi = models.CharField(max_length=200, null=True)
    Hinhanh =models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.Ten
class Giohang(models.Model):
    date_oder = models.DateTimeField(auto_now_add=True)
    Complete = models.BooleanField(default=False,null=True, blank=False)

    def __str__(self):
        return str(self.id)
class Giohang_items(models.Model):
    phong = models.ForeignKey(Phong, on_delete=models.SET_NULL, blank=True, null=True)
    giohang = models.ForeignKey(Giohang, on_delete=models.SET_NULL, blank=True, null=True)
    soluong = models.IntegerField(default=0,null=True, blank=True)
    date_them = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Ten