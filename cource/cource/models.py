from django.db import models
from student.models import Student
from teacher.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    credits = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name}"
