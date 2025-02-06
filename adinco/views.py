from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm

def home(request):
    return render(request, 'home.html')

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions_list.html', {'questions': questions})

def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question-detail', pk=form.instance.id)
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form': form})

def edit_question(request, pk):
    question= get_object_or_404(Question, id=pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance = question)
        if form.is_valid():
            form.save()
            return redirect('question-detail')
    else:
        form = QuestionForm(instance = question)
    return render(request, 'edit_question.html', {'form': form})

def delete_question(request, pk):
    question = get_object_or_404(Question, id=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('questions-list')
    return render(request, 'delete_question.html', {'question': question})

def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    return render(request, 'question_detail.html', {'question': question})
