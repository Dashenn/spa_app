from django.db import models


class Specialist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    experience_years = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="specialists/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", null=True, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="services"
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Review by {self.first_name} {self.last_name} ({self.rating})"


class Request(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_submitted = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    desired_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Request from {self.first_name} {self.last_name}"
