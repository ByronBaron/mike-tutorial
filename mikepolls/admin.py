from django.contrib import admin
from mikepolls.models import Choice, Question
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
