from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('questions/', question_list, name='questions-list'),
    path('add-question/', ask_question, name='add-question'),   
    path('edit-question/<int:pk>/', edit_question, name='edit-question'),
    path('delete-question/<int:pk>/', delete_question, name='delete-question'),
    path('question-detail/<int:pk>/', question_detail, name='question-detail'),

]