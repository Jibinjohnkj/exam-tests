from authentication.models import User
from .models import Exam, Question, Option
from django.http import Http404

def process_results(users, exam=1):
    results = []
    try:
        exam = Exam.objects.get(id=exam)
    except Exam.DoesNotExist:
        raise Http404("Exam does not exist")

    for user_id in users:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        percentage = calculate_percentage(user, exam=exam)
        results.append({
            'user':user,
            'percentage':percentage,
            'passed':percentage >= exam.pass_percentage
        })
    return results


def calculate_percentage(user, exam):
    questions = Question.objects.filter(exam=exam)
    total_questions = questions.count()
    questions_rightly_answered = 0
    for question in questions:
        # if all right options were selected and no wrong options were selected,
        # the answer is correct
        right_options = Option.objects.filter(question=question, is_right_option=True)
        user_choices = Option.objects.filter(question=question, useranswer__student=user)
        if set(user_choices) == set(right_options):
            questions_rightly_answered+=1

    return (questions_rightly_answered*100)/total_questions