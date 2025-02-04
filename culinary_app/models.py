from django.db import models
from django.contrib.auth.models import User

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_method = models.TextField()
    photo = models.ImageField(upload_to='dishes/', null=True, blank=True)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.dish.name} - {self.score}"
