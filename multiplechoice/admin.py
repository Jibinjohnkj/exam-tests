from django.contrib import admin

from multiplechoice.models import Exam, Question, Option, UserAnswer

class OptionInline(admin.StackedInline):
    model = Option
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('description',' exam__title','exam__teacher')
    list_display = ('description','exam__title','exam__teacher','updated_on')
    inlines = [OptionInline]

    def exam__title(self, obj):
        return obj.exam.title

    def exam__teacher(self, obj):
        return obj.exam.teacher

admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam)
admin.site.register(UserAnswer)
