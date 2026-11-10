from django.db import models

# Create your models here.
DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

class Question(models.Model):
    text = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): # __str__ method for better representation
        return f'[{self.difficulty}] {self.text[:50]}...'

    