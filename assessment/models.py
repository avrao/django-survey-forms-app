from django.db import models
from defect_notice.models import SiteDetailsLookup

class Assessment(models.Model):
        assessment_id = models.AutoField(primary_key=True)
        assessmentName = models.CharField(max_length=100)
        assessmentPosition = models.IntegerField()

        def __unicode__(self):
            return unicode(self.assessmentName)

        class Meta:
                db_table = 'assessment'

class Category(models.Model):
        category_id = models.AutoField(primary_key=True)
        categoryName = models.CharField(max_length=100)
        categoryPosition = models.IntegerField()

        # every category belongs to an parent assessment
        assessment = models.ForeignKey(Assessment)

        def __unicode__(self):
            return unicode(self.categoryName)

        class Meta:
                db_table = 'category'

class Question(models.Model):
        question_id = models.AutoField(primary_key=True)
        questionText = models.CharField(max_length=250)
        guidelineText = models.CharField(max_length=250)
        # category is like template, and we know each
        # question belongs to a parent template
        category = models.ForeignKey(Category)

        class Meta:
                db_table = 'question'


"""
A response summary is provided by a user. for a site-code, for a period, for an assesment.
Response details will have multiple responses (each of which has a question
behind it.
"""
class ResponseSummary(models.Model):
        summary_id=models.AutoField(primary_key=True)
        username = models.CharField(max_length=200)
        siteCode = models.ForeignKey(SiteDetailsLookup)
        assessmentDate = models.DateField(auto_now=False)
        # eg. 'Monthly: 06-2014' , or 'Q1: 2014'
        period = models.CharField(max_length=20)
        status = models.CharField(max_length=128)
        assessment = models.ForeignKey(Assessment)

        class Meta:
                db_table = 'responseSummary'


class ResponseDetail(models.Model):
        detail_id = models.AutoField(primary_key=True)
        summary = models.ForeignKey(ResponseSummary)
        question = models.ForeignKey(Question)
        score= models.IntegerField()

        class Meta:
                db_table='responseDetail'
