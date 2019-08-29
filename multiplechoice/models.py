from django.db import models
from authentication.models import User


class Exam(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    pass_percentage = models.FloatField()
    date = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam.title + ' => ' + self.description


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    is_right_option = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class UserAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Option, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('student', 'answer'),)

    def __str__(self):
        return self.student.first_name + ' => ' + self.answer.description


