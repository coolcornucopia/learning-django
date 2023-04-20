from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # Re-order the fields (ie. by-pass the default order)
    fields = ["pub_date", "question_text"]

# Let admin constructing a default form representation of our Question model
admin.site.register(Question, QuestionAdmin)
