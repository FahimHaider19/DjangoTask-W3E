from django.db import models

# Create your models here.
class Product(models.Model):
    id
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.TextField(null=True)
    publisher = models.CharField(max_length=200, null=True)
    developer = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    titleimage = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=200, null=True)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Review for {self.product.name} by {self.user}"