from django.db import models
from django.utils.text import slugify
from employe.models import Employe
from django.contrib.auth.models import User
# Create your models here.

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

class Color(models.Model):
    code = models.CharField(max_length=2,unique=True,verbose_name='الكود')
    name = models.CharField( max_length=50,verbose_name='الاسم')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اللون'
        verbose_name_plural = 'الالوان'

class Category(models.Model):
    code = models.CharField(max_length=2,unique=True,verbose_name='الكود')
    name = models.CharField( max_length=50,verbose_name='الاسم')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'النوع'
        verbose_name_plural = 'الانواع'

class Type(models.Model):
    code = models.CharField(max_length=2,unique=True,verbose_name='الكود')
    name = models.CharField( max_length=50,verbose_name='الاسم')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'الصنف'
        verbose_name_plural = 'الاصناف'

class creator(models.Model):
    code = models.CharField(max_length=4,unique=True,verbose_name='الكود')
    name = models.CharField( max_length=50,verbose_name='الاسم')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'المصنع'
        verbose_name_plural = 'المصانع'


def image_upload(instance ,filename):
    imgname , extintion = filename.split('.')
    return 'Products/%s.%s'%(instance.id,extintion)

class Product(models.Model):
    barcode = models.SlugField(("الباركود"),max_length = 20,blank=True, null=True,unique=True)
    barcode_IMG = models.ImageField(("صورة الباركود"),upload_to='Barcodes/',blank=True)
    name = models.ForeignKey(creator, verbose_name=("الاسم"), on_delete=models.CASCADE)
    img = models.ImageField(("الصوره"),upload_to=image_upload,default='default.png')
    typ = models.ForeignKey(Type, verbose_name=("النوع"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("الصنف"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("اللون"), on_delete=models.CASCADE)
    size = models.IntegerField(verbose_name=("المقاس"))
    quantity = models.IntegerField(verbose_name=("الكميه"))
    priceIn = models.FloatField(verbose_name=("سعر الشراء"))
    priceOut = models.FloatField(verbose_name=("سعر البيع"))
    active  = models.BooleanField(verbose_name=("متاح") ,default=True)
    date_published = models.DateField(verbose_name=("تاريخ الاضافه"), auto_now=False, auto_now_add=True)
    
    def save(self, *args, **kwargs):
         if not self.barcode:
            string =str(self.name.code)+str(self.typ.code)+str(self.category.code)+str(self.color.code)+str(self.size)
            self.barcode = slugify(string)

         EAN = barcode.get_barcode_class('code128')
         ean = EAN(f'{self.barcode}', writer=ImageWriter())
         buffer = BytesIO()
         ean.write(buffer)
         self.barcode_IMG.save(f'{self.barcode}.png', File(buffer), save=False) 
         super(Product, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        string = str(self.typ)+' '+str(self.category)+' '+str(self.name)
        return string
    class Meta:
        verbose_name = 'المنتج'
        verbose_name_plural = 'المنتجات'

class OrderItem(models.Model):
    user  = models.ForeignKey(User, verbose_name=("الكاشير"), on_delete=models.CASCADE)
    ordered  = models.BooleanField(default=False)
    item = models.ForeignKey(Product, verbose_name=("المنتج"), on_delete=models.CASCADE)
    quantity = models.IntegerField(("الكميه"),default=1)
    def __str__(self):
        return str(self.quantity)+' '+str(self.item) 
    class Meta:
        verbose_name = 'المباع'
        verbose_name_plural = 'المباع'
    def getTotal(self):
        return self.quantity*self.item.priceOut

class Order(models.Model):
    user  = models.ForeignKey(User, verbose_name=("الكاشير"), on_delete=models.CASCADE)
    emp  = models.ForeignKey(Employe,blank=True, null=True, verbose_name=("البائع"), on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, verbose_name=("المنتجات المباعه"))
    order_date = models.DateTimeField(("وقت البيع"),auto_now_add=True)
    ordered  = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)

    def getTotalall(self):
        total =0
        for item in self.items.all():
            total += item.getTotal()
        return total
    def get_products(self):
        return "\n".join([str(p) for p in self.items.all()])

    class Meta:
        verbose_name = 'الفاتوره'
        verbose_name_plural = 'الفواتير'