from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Re-order the fields (ie. by-pass the default order)
    # Split the form up into fieldsets
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


# Let admin constructing a default form representation of our Question model
admin.site.register(Question, QuestionAdmin)
