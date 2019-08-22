from django.db import models
from django.contrib.postgres.fields import ArrayField

class types(models.Model):
    name = models.CharField(max_length=50, verbose_name="نوع محصول")
    unit = models.CharField(max_length=20, verbose_name="واحد اندازه گیری")
    display_on_home = models.CharField(max_length=5, choices=[('بله','بله'),('خیر','خیر')],default='بله', verbose_name="نمایش در صفحه اول")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "انواع محصولات"
        

class brands(models.Model):
    name = models.CharField(max_length=30, verbose_name="برند")
    display_on_home = models.CharField(max_length=5, choices=[('بله','بله'),('خیر','خیر')],default='بله', verbose_name="نمایش در صفحه اول")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "برندها"


class product(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام")
    price = models.IntegerField(verbose_name='قیمت')
    Type = models.ForeignKey(types, on_delete=models.CASCADE,verbose_name='نوع محصول')
    brand = models.ForeignKey(brands, on_delete=models.CASCADE,verbose_name='شرکت')
    image = models.ImageField(default='tools/default.jpg', upload_to='tools',verbose_name='تصویر')
    size = models.CharField(max_length=20, verbose_name="سایز",default='None')
    explain = models.TextField(default="!توضیحی وجود ندارد", verbose_name='توضیحات')
    rate = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], verbose_name='امتیاز')
    def full_star_rating(self):
        return range(self.rate)
    def empty_star_rating(self):
        return range(5-self.rate)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "محصولات"


class order(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    size = models.CharField(max_length=20, null=True, blank=True)
    amount = models.FloatField()
    def __str__(self):
        return str(self.id)
    def total_price(self):
        return int(self.product.price * self.amount)
