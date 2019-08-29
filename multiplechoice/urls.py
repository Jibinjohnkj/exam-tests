from django.urls import path

from .views import QuestionView, ResultView

urlpatterns = [
    path('exam/<int:exam_id>/question/<int:question_id>/', QuestionView.as_view(), name='question'),
    path('exam/<int:exam_id>/result/', ResultView.as_view(), name='result'),
]