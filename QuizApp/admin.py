from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizAttempt)
admin.site.register(AttemptAnswer)
admin.site.register(AISettings)