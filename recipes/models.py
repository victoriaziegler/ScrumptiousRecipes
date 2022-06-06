from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " by " + self.author


class Step(models.Model):
    order = models.PositiveSmallIntegerField()
    directions = models.TextField(max_length=300)
    recipe = models.ForeignKey(
        "Recipe", related_name="steps", on_delete=models.CASCADE
    )
    food_items = models.ManyToManyField("FoodItem", blank=True)


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.abbreviation


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(20), MinValueValidator(1)]
    )

    recipe = models.ForeignKey(
        "Recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    def __str__(self):
        amount_str = str(self.amount)
        return (
            amount_str
            + " "
            + self.measure.abbreviation
            + " of "
            + self.food.name
        )


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    recipe = models.ForeignKey(
        "Recipe", related_name="ratings", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.value)
