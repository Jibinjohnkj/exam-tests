from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import Http404
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Exam, Question, Option, UserAnswer
from .utils import process_results

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        """
        If student, show option to Take Test
        If teacher, show option to 'Create Test' or 'See Results'
        """

        context = {'user': request.user,
                   'exams': Exam.objects.all()}
        return render(request, 'multiplechoice/index.html', context)


class QuestionView(LoginRequiredMixin, View):
    def get(self, request, exam_id=None, question_id=None):
        """
        Display the question according to the id in the URL
        """
        if question_id:
            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                raise Http404("Question not exist")

        context = {'user': request.user,
                   'question': question}
        return render(request, 'multiplechoice/question.html', context)

    def post(self, request, exam_id=None, question_id=None):
        """
        Save the answers given by the student and redirect to next question
        If all questions answered redirect to result
        """

        # Save the answers given by the student
        user = request.user
        options = request.POST.getlist("selected-options")

        for item in options:
            try:
                option = Option.objects.get(id=item)
            except Option.DoesNotExist:
                raise Http404("Illegal option detected")

            try:
                UserAnswer.objects.create(student=user, answer=option)
            except IntegrityError:
                raise Http404("You already answered this question")

        next_question = question_id + 1
        if Question.objects.filter(exam__id=exam_id, id=next_question).exists():
            # Redirect to next question
            return redirect(reverse('question', kwargs={'exam_id': exam_id,
                                                     'question_id':next_question}))
        else:
            # If all questions answered redirect to result
            return redirect(reverse('result', kwargs={'exam_id': exam_id}))


class ResultView(LoginRequiredMixin, View):
    def get(self, request, exam_id):
        """
        If a student, show his results
        If a teacher, show results of all student who have taken
        """

        users = []
        user = request.user
        if user.type == 'Teacher':
            # Get all users who took the test
            pupils = UserAnswer.objects.filter(answer__question__exam__id=exam_id
                                      ).values_list('student__id', flat=True)
            users.extend(set(pupils))
        else:
            users.append(user.id)

        context = {'results':process_results(users, exam_id)}

        return render(request, 'multiplechoice/result.html', context)
