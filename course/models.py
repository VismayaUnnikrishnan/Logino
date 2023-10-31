from django.db import models

# Create your models here.

class Course(models.Model):
    COURSE_CATEGORIES = (
        ('Short', 'Short Course'),
        ('Long', 'Long Course'),
    )
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=COURSE_CATEGORIES)

    def __str__(self) -> str:
        return self.course_name