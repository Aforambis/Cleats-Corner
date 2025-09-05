from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=40)
    is_featured = models.BooleanField(default=False)

    brand = models.CharField(max_length=80)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.brand} {self.name}"

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.IntegerField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Size {self.size} ({self.stock} left)"