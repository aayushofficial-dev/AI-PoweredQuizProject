from django.db import models

# Create your models here.
DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

class Question(models.Model):
    text = models.CharField(max_length=500)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): # __str__ method for better representation
        return f'[{self.difficulty}] {self.text[:50]}...'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    player_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    total_questions = models.PositiveIntegerField(default=10)
    score = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_limit_seconds = models.PositiveIntegerField(default=300) # default 5 minutes
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.player_name} - ({self.difficulty})"

class AttemptAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    order = models.PositiveIntegerField() 
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)
    ai_explanation = models.TextField(blank=True, default="")
    ai_learn_more = models.TextField(blank=True, default="")
    
    def __str__(self):
        return f"Attempt {self.attempt.id} - Q{self.order}"

class AISettings(models.Model):
    gemini_api_key = models.TextField(blank=True, default="")
    gemini_model = models.CharField(max_length=100, default='gemini-2.5-flash')
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'AI settings'

    @classmethod
    def get_solo(cls): # singleton pattern to ensure only one settings object 
        obj, _ = cls.objects.get_or_create(id=1)
        return obj

 