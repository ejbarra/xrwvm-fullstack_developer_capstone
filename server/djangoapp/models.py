# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Additional optional fields
    country = models.CharField(max_length=50, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    # Type choices for the car
    TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    ]
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(
        CarMake, 
        on_delete=models.CASCADE,
        related_name='car_models'
    )
    # Dealer ID - refers to dealer in Cloudant database
    dealer_id = models.IntegerField()
    # Required fields
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='SUV'
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    # Additional optional fields
    color = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name}"
