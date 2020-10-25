from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.CharField(max_length=200,unique=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        vaerbose_name_plural='categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_lengh=200,db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name
