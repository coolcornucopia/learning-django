from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # Re-order the fields (ie. by-pass the default order)
    # Split the form up into fieldsets
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

# Let admin constructing a default form representation of our Question model
admin.site.register(Question, QuestionAdmin)
