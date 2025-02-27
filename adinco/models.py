from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer_text


# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
