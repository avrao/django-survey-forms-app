from django.db import models
from defect_notice.models import SiteDetailsLookup
from datetime import date


class Assessment(models.Model):
    ASSESSMENT_PERIOD = (
        ('Monthly, 1'),
        ('Quarterly', '2')
    )
    title_id = models.AutoField(primary_key=True)
    titleName = models.CharField(max_length=128)
    period = models.CharField(max_length=1, choices=ASSESSMENT_PERIOD)

    def __unicode__(self):
        return self.titleName,self.title_id

    class Meta:
        db_table = 'assessment'


"""
A category is like a template for a questionnaire.
It contains multiple questions for which responses are saved.
Currently, there are 5 categories that together form one complete assessment
"""
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=128)

    def __unicode__(self):
        return self.categoryName, self.category_id

    class Meta:
        db_table = 'category'

"""
A question is part of a Category object.
A Category object will contain multiple questions
"""
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    title = models.ForeignKey(Assessment)
    category = models.ForeignKey(Category)
    questionText = models.CharField(max_length=256)
    guidelineText = models.CharField(max_length=400, null=True)

    class Meta:
        db_table = 'question'

class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    score = models.IntegerField()
    username = models.CharField(max_length=128)
    siteCode = models.ForeignKey(SiteDetailsLookup)
    Status = models.CharField(max_length=128)
    responseDate = models.DateField(auto_now=False)

    class Meta:
        db_table = 'response'

# class UserResponseInfo(models.Model):
#     userResponseInfo_id = models.AutoField(primary_key=True)
#     response = models.ForeignKey(Response)
#     username = models.CharField(max_length=128)
#     siteCode = models.ForeignKey(SiteDetailsLookup)
#     Status = models.CharField(max_length=128)
#     responseDate = models.DateField(auto_now=False)
