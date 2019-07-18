from django.db import models

class types(models.Model):
    name = models.CharField(max_length=50, verbose_name="نوع محصول")
    unit = models.CharField(max_length=20, verbose_name="واحد اندازه گیری")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "انواع محصولات"
        

class brands(models.Model):
    name = models.CharField(max_length=30, verbose_name="برند")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "برندها"

class product(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام")
    Type = models.ForeignKey(types, on_delete=models.CASCADE)
    brand = models.ForeignKey(brands, on_delete=models.CASCADE)
    image = models.ImageField(default='tools/default.jpg', upload_to='tools')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "محصولات"