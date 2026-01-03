from django.db import models

class Lead(models.Model):
    SEX_CHOICES = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
    )

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    location = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
