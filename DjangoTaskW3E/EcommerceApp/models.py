from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.
class Product(models.Model):
    id
    name = models.CharField(max_length=200, validators=[MinLengthValidator(2)], unique=True, null=False, blank=False)
    price = models.FloatField(validators=[MinValueValidator(0.0) ,MaxValueValidator(9999.0)], null=False, blank=False, default=0)
    description = models.TextField(validators=[MinLengthValidator(10)], null=True)
    publisher = models.CharField(max_length=200, validators=[MinLengthValidator(2)], null=False, blank=False)
    developer = models.CharField(max_length=200, validators=[MinLengthValidator(2)], null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    titleimage = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=200, validators=[MinLengthValidator(2)], null=False, blank=False,  default="Anonymous")
    text = models.TextField(max_length=10000, validators=[MinLengthValidator(3)], null=False, blank=False)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0.0) ,MaxValueValidator(5.0)])
    
    def __str__(self):
        return f"Review for {self.product.name} by {self.user}"