from django.contrib import admin
from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4 # Number of extra choice fields to display

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'difficulty', 'text')
    search_fields = ('text',)
    list_filter = ('difficulty',)
    inlines = [ChoiceInline]

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'difficulty', 'score', 'total_questions',)
    search_fields = ('player_name',)
    list_filter  = ('difficulty', 'started_at', 'completed_at')
    readonly_fields = ('started_at', 'completed_at', 'score', 'total_questions')

@admin.register(AISettings)
class AISettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gemini_model', 'update_at')
    readonly_fields = ('update_at',)

@admin.register(AttemptAnswer)
class AttemptAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt', 'question', 'order', 'selected_choice', 'is_correct', 'ai_explanation', 'ai_learn_more')
    search_fields = ('attempt__player_name', 'question__text')
    list_filter = ('is_correct', )

