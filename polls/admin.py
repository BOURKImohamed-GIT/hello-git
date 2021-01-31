from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Question,Choice
# admin.site.register([Question,Choice])

class QuestionAdmin(TranslationAdmin):
      model=Question


class ChoiceAdmin(TranslationAdmin):
      model=Choice

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)