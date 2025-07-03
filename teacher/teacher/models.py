from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name
