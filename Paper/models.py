# Create your models here.
from django.db import models
from curriculum.models import subjectdetails



#class Subject(models.Model):

    #id = models.AutoField(primary_key=True)
    #subjectname = models.CharField(max_length=100)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    #def __str__(self):
        #return self.subjectname


class Papers(models.Model):

    id = models.AutoField(primary_key=True)
    paper_name = models.CharField(max_length=100)
    subject_id = models.ForeignKey(subjectdetails, on_delete=models.PROTECT,verbose_name='Subject', db_column='subject_id')
    paper_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.paper_name
