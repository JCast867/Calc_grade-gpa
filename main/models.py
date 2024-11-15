from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GRADE_TO_GPA = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0,
}

class Class(models.Model):
    GRADE_CHOICES = [
        ('A-', 'A-'),
        ('A', 'A'),
        ('A+', 'A+'),  # Exclude A+ later
        ('B-', 'B-'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('C-', 'C-'),
        ('C', 'C'),
        ('C+', 'C+'),
        ('D-', 'D-'),
        ('D', 'D'),
        ('D+', 'D+'),
        ('F', 'F'),
        # Exclude F- as it's not a standard grade
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.grade} ({self.credits} credits)"