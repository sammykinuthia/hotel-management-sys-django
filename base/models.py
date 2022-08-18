from django.db import models


class Category(models.Model):
    CATEGORIES = [
        ("BUSINESS", "BUSINESS"),
        ("ECONOMIC", "ECONOMIC"),
        ("LOW", "LOW")
    ]
    BEDS = [
        (1, 'one'),
        (2, 'two'),
    ]
    categories = models.CharField(max_length=10, choices=CATEGORIES)
    beds = models.IntegerField(choices=BEDS)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.categories} {self.beds}"


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    room_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.category} {self.room_code}"


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    city = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=16)
    id_number = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    book_date = models.DateTimeField(auto_now=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
