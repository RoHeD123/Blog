from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default="example@example.com")
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    enrolled_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.full_name
