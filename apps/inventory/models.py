from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = (
        ("coffee", "Coffee"),
        ("tea", "Tea"),
        ("sugar", "Sugar"),
        ("cup", "Cup"),
        ("other", "Other"),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
