from django.contrib import admin

from multiplechoice.models import Exam, Question, Option

class OptionInline(admin.StackedInline):
    model = Option
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('description',' exam__title', 'exam__teacher')
    list_display = ('exam__title', 'exam__teacher', 'updated_on')
    inlines = [OptionInline]

    def exam__title(self, obj):
        return obj.exam.title

    def exam__teacher(self, obj):
        return obj.exam.teacher


#class ExamAdmin(admin.ModelAdmin):
    #list_display = ('title', 'teacher', 'date', 'updated_on')


#admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)

