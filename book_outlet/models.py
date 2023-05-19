from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Country Entries"

class Address(models.Model):
    street = models.CharField(max_length= 80)
    postal_code = models.CharField(max_length=5)
    city= models.CharField(max_length= 50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code} , {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    address = models.OneToOneField(Address , on_delete=models.CASCADE , null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class book(models.Model) :
    title = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author= models.ForeignKey(Author, on_delete=models.CASCADE , null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True ,null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title} ({self.rating})"