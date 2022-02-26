from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, max_length=200)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name




class Product(models.Model):

    colors = (
        ('red','Red'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White')
    )
    categories = (
        ("1", "Electronics"),
        ("2", "Jewellery"),
        ("3", " Men Clothing"),
        ("4", "Women Clothing")
    )
    inStock = (("yes","Yes"), ("no", "No"),("limited","Limited (< 10 )"))
    title = models.CharField(blank=False,max_length=200)
    description = models.TextField(blank=True,max_length=1000)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE, choices=categories, default="")
    colors = models.CharField(max_length=20, choices=colors, default="black")
    available = models.IntegerField(default=0)
    inStock = models.CharField(default="No",choices=inStock, max_length=20)
    added_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-title","price","-added_on")