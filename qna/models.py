from django.db import models
from django import forms

# Create your models here.

'''
class Subject(models.Model):

    id = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subjectname
'''
from Paper.models import Papers

# class Papers(models.Model):
#
#     id = models.AutoField(primary_key=True)
#     paper_name = models.CharField(max_length=100)
#     subject_id = models.IntegerField()
#     paper_desc = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.paper_name


class Questionanswers(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.ForeignKey(Papers, on_delete=models.PROTECT, verbose_name='Papers')
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "question_answers"
