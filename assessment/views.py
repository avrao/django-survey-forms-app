# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

#the below import is needed to load AJAX:
from django.template.loader import get_template

from django.core.context_processors import csrf
from forms import *
from models import *
import json
from django.core import mail
from django.core.mail import send_mail
import datetime


# Create your views here.
def test(request):
    return HttpResponse("testing assessment page app: Passed")

# class MonthlyAssessmentWizard(SessionWizardView):
#     template_name = "assessment/step.html"
#     def done(self, form_list, **kwargs):
#
#         form_data = process_form_data(self, form_list)
#
#         return render_to_response('assessment/done.html')

# def process_form_data(self, form_list):
#     context = RequestContext(self.request)
#     form_data = [form.cleaned_data for form in form_list]
#
#     form1 = MonthlyAssessForm1(self.request.POST)
#     #form2 = MonthlyAssessForm2(self.request.POST)
#     if form1 and self.request.POST == 'SUBMIT':
#
#         assObj= Assessment.objects.get(assessment_id=form_data[0]['assessment_id'])
#         period = date.today().strftime('%m-%Y')
#         #saving to database here
#         # if self.request.method == 'POST' and form.is_valid():
#         saveform1_username = form_data[0]['username']
#         saveform1_siteCode = form_data[0]['siteCode']
#         saveform1_assessmentDate = form_data[0]['assessmentDate']
#         saveform1_assessment = assObj
#         saveform1_questionid1 = form_data[0]['question_id1']
#         saveform1_questionid2 = form_data[0]['question_id2']
#         saveform1_period = str('Monthly: ' + period)
#         saveform1_score_1 = self.request.POST.get('radio_1').strip(u'/')
#         saveform1_score_2 = self.request.POST.get('radio_2').strip(u'/')
#
#         saveResponseSummaryform1 = ResponseSummary(username=saveform1_username, siteCode=saveform1_siteCode, assessmentDate=saveform1_assessmentDate,  period=saveform1_period, assessment=saveform1_assessment)
#         saveResponseSummaryform1.save()
#
#         getpk= saveResponseSummaryform1._get_pk_val()
#         summaryObj = ResponseSummary.objects.get(summary_id=getpk)
#         questionObj1 = Question.objects.get(question_id=saveform1_questionid1)
#         questionObj2 = Question.objects.get(question_id=saveform1_questionid2)
#
#         saveResponseDetailsq1 = ResponseDetail(summary=summaryObj, question=questionObj1, score_=int(saveform1_score_1))
#         saveResponseDetailsq1.save()
#
#         saveResponseDetailsq2 = ResponseDetail(summary=summaryObj, question=questionObj2, score_=int(saveform1_score_2))
#         saveResponseDetailsq2.save()
#     # elif form2:
#     #     #save form2 score_s
#
#     #
#     # msg= "Successfully Assessment completed by: " + str(saveform1_username) + " on " + str(saveform1_assessmentDate) + " for " + str(saveform1_siteCode) + " , " + str(saveform1_period)
#     # variables= RequestContext(self.request,{'msg': msg})
#     # return render_to_response('assessment/done.html', variables)
#     return form_data


class MonthlyAssessmentWizard(SessionWizardView):
    template_name = "assessment/step.html"

    def done(self, form_list, **kwargs):

        # form_data = process_form_data(self, form_list)
        form_data = process_form_data(self, form_list)
        return render_to_response('assessment/done.html', {'form_data': form_data})

def process_form_data(self, form_list):
    context = RequestContext(self.request)
    form_data = [form.cleaned_data for form in form_list]

    form1 = MonthlyAssessForm1(self.request.POST)
    form2 = MonthlyAssessForm2(self.request.POST)
    form3 = MonthlyAssessForm2(self.request.POST)
    form4 = MonthlyAssessForm2(self.request.POST)
    form5 = MonthlyAssessForm2(self.request.POST)

    #form1 fields:
    assObj= Assessment.objects.get(assessment_id=form_data[0]['assessment_id'])
    #period = date.today().strftime('%m-%Y')
    #saving to database here
    saveform1_username = form_data[0]['username']
    saveform1_siteCode = form_data[0]['siteCode']
    saveform1_assessmentDate = form_data[0]['assessmentDate']
    saveform1_assessment = assObj
    questionObj1 = Question.objects.get(question_id=form_data[0]['question_id1'])
    questionObj2 = Question.objects.get(question_id=form_data[0]['question_id2'])
    questionObj3 = Question.objects.get(question_id=form_data[0]['question_id3'])
    questionObj4 = Question.objects.get(question_id=form_data[0]['question_id4'])
    questionObj5 = Question.objects.get(question_id=form_data[0]['question_id5'])
    questionObj6 = Question.objects.get(question_id=form_data[0]['question_id6'])
    questionObj7 = Question.objects.get(question_id=form_data[0]['question_id7'])
    questionObj8 = Question.objects.get(question_id=form_data[0]['question_id8'])
    questionObj9 = Question.objects.get(question_id=form_data[0]['question_id9'])
    questionObj10 = Question.objects.get(question_id=form_data[0]['question_id10'])
    questionObj11 = Question.objects.get(question_id=form_data[0]['question_id11'])
    questionObj12 = Question.objects.get(question_id=form_data[0]['question_id12'])
    questionObj13 = Question.objects.get(question_id=form_data[0]['question_id13'])
    questionObj14 = Question.objects.get(question_id=form_data[0]['question_id14'])
    questionObj15 = Question.objects.get(question_id=form_data[0]['question_id15'])
    questionObj16 = Question.objects.get(question_id=form_data[0]['question_id16'])

    saveform1_score_1 = form_data[0]['score_1']
    saveform1_score_2 = form_data[0]['score_2']
    saveform1_score_3 = form_data[0]['score_3']
    saveform1_score_4 = form_data[0]['score_4']
    saveform1_score_5 = form_data[0]['score_5']
    saveform1_score_6 = form_data[0]['score_6']
    saveform1_score_7 = form_data[0]['score_7']
    saveform1_score_8 = form_data[0]['score_8']
    saveform1_score_9 = form_data[0]['score_9']
    saveform1_score_10 = form_data[0]['score_10']
    saveform1_score_11 = form_data[0]['score_11']
    saveform1_score_12 = form_data[0]['score_12']
    saveform1_score_13 = form_data[0]['score_13']
    saveform1_score_14 = form_data[0]['score_14']
    saveform1_score_15 = form_data[0]['score_15']
    saveform1_score_16 = form_data[0]['score_16']
    saveform1_period = form_data[0]['period']
    saveform1_status = str('Complete')

    #form2 fields:
    questionObj17 = Question.objects.get(question_id=form_data[1]['question_id17'])
    questionObj18 = Question.objects.get(question_id=form_data[1]['question_id18'])
    questionObj19 = Question.objects.get(question_id=form_data[1]['question_id19'])
    questionObj20 = Question.objects.get(question_id=form_data[1]['question_id20'])
    questionObj21 = Question.objects.get(question_id=form_data[1]['question_id21'])
    questionObj22 = Question.objects.get(question_id=form_data[1]['question_id22'])
    questionObj23 = Question.objects.get(question_id=form_data[1]['question_id23'])
    questionObj24 = Question.objects.get(question_id=form_data[1]['question_id24'])
    questionObj25 = Question.objects.get(question_id=form_data[1]['question_id25'])
    questionObj26 = Question.objects.get(question_id=form_data[1]['question_id26'])
    questionObj27 = Question.objects.get(question_id=form_data[1]['question_id27'])
    questionObj28 = Question.objects.get(question_id=form_data[1]['question_id28'])
    questionObj29 = Question.objects.get(question_id=form_data[1]['question_id29'])
    questionObj30 = Question.objects.get(question_id=form_data[1]['question_id30'])
    saveform2_score_17 = form_data[1]['score_17']
    saveform2_score_18 = form_data[1]['score_18']
    saveform2_score_19 = form_data[1]['score_19']
    saveform2_score_20 = form_data[1]['score_20']
    saveform2_score_21 = form_data[1]['score_21']
    saveform2_score_22 = form_data[1]['score_22']
    saveform2_score_23 = form_data[1]['score_23']
    saveform2_score_24 = form_data[1]['score_24']
    saveform2_score_25 = form_data[1]['score_25']
    saveform2_score_26 = form_data[1]['score_26']
    saveform2_score_27 = form_data[1]['score_27']
    saveform2_score_28 = form_data[1]['score_28']
    saveform2_score_29 = form_data[1]['score_29']
    saveform2_score_30 = form_data[1]['score_30']

    #form3 fields:
    questionObj31 = Question.objects.get(question_id=form_data[2]['question_id31'])
    questionObj32 = Question.objects.get(question_id=form_data[2]['question_id32'])
    questionObj33 = Question.objects.get(question_id=form_data[2]['question_id33'])
    questionObj34 = Question.objects.get(question_id=form_data[2]['question_id34'])
    questionObj35 = Question.objects.get(question_id=form_data[2]['question_id35'])
    questionObj36 = Question.objects.get(question_id=form_data[2]['question_id36'])
    questionObj37 = Question.objects.get(question_id=form_data[2]['question_id37'])
    questionObj38 = Question.objects.get(question_id=form_data[2]['question_id38'])
    saveform3_score_31 = form_data[2]['score_31']
    saveform3_score_32 = form_data[2]['score_32']
    saveform3_score_33 = form_data[2]['score_33']
    saveform3_score_34 = form_data[2]['score_34']
    saveform3_score_35 = form_data[2]['score_35']
    saveform3_score_36 = form_data[2]['score_36']
    saveform3_score_37 = form_data[2]['score_37']
    saveform3_score_38 = form_data[2]['score_38']

    #form4 fields:
    questionObj39 = Question.objects.get(question_id=form_data[3]['question_id39'])
    questionObj40 = Question.objects.get(question_id=form_data[3]['question_id40'])
    questionObj41 = Question.objects.get(question_id=form_data[3]['question_id41'])
    questionObj42 = Question.objects.get(question_id=form_data[3]['question_id42'])
    questionObj43 = Question.objects.get(question_id=form_data[3]['question_id43'])
    questionObj44 = Question.objects.get(question_id=form_data[3]['question_id44'])
    questionObj45 = Question.objects.get(question_id=form_data[3]['question_id45'])
    questionObj46 = Question.objects.get(question_id=form_data[3]['question_id46'])
    saveform4_score_39 = form_data[3]['score_39']
    saveform4_score_40 = form_data[3]['score_40']
    saveform4_score_41 = form_data[3]['score_41']
    saveform4_score_42 = form_data[3]['score_42']
    saveform4_score_43 = form_data[3]['score_43']
    saveform4_score_44 = form_data[3]['score_44']
    saveform4_score_45 = form_data[3]['score_45']
    saveform4_score_46 = form_data[3]['score_46']

    #form5 fields:
    questionObj47 = Question.objects.get(question_id=form_data[4]['question_id47'])
    questionObj48 = Question.objects.get(question_id=form_data[4]['question_id48'])
    questionObj49 = Question.objects.get(question_id=form_data[4]['question_id49'])
    questionObj50 = Question.objects.get(question_id=form_data[4]['question_id50'])
    questionObj51 = Question.objects.get(question_id=form_data[4]['question_id51'])
    saveform5_score_47 = form_data[4]['score_47']
    saveform5_score_48 = form_data[4]['score_48']
    saveform5_score_49 = form_data[4]['score_49']
    saveform5_score_50 = form_data[4]['score_50']
    saveform5_score_51 = form_data[4]['score_51']

    if form1:
        saveResponseSummaryform1 = ResponseSummary(username=saveform1_username, siteCode=saveform1_siteCode, assessmentDate=saveform1_assessmentDate,  period=saveform1_period, status=saveform1_status, assessment=saveform1_assessment)
        saveResponseSummaryform1.save()

        getpk= saveResponseSummaryform1._get_pk_val()
        summaryObj = ResponseSummary.objects.get(summary_id=getpk)

        saveResponseDetailsq1 = ResponseDetail(summary=summaryObj, question=questionObj1, score=int(saveform1_score_1))
        saveResponseDetailsq1.save()

        saveResponseDetailsq2 = ResponseDetail(summary=summaryObj, question=questionObj2, score=int(saveform1_score_2))
        saveResponseDetailsq2.save()

        saveResponseDetailsq3 = ResponseDetail(summary=summaryObj, question=questionObj3, score=int(saveform1_score_3))
        saveResponseDetailsq3.save()

        saveResponseDetailsq4 = ResponseDetail(summary=summaryObj, question=questionObj4, score=int(saveform1_score_4))
        saveResponseDetailsq4.save()

        saveResponseDetailsq5 = ResponseDetail(summary=summaryObj, question=questionObj5, score=int(saveform1_score_5))
        saveResponseDetailsq5.save()

        saveResponseDetailsq6 = ResponseDetail(summary=summaryObj, question=questionObj6, score=int(saveform1_score_6))
        saveResponseDetailsq6.save()

        saveResponseDetailsq7 = ResponseDetail(summary=summaryObj, question=questionObj7, score=int(saveform1_score_7))
        saveResponseDetailsq7.save()

        saveResponseDetailsq8 = ResponseDetail(summary=summaryObj, question=questionObj8, score=int(saveform1_score_8))
        saveResponseDetailsq8.save()

        saveResponseDetailsq9 = ResponseDetail(summary=summaryObj, question=questionObj9, score=int(saveform1_score_9))
        saveResponseDetailsq9.save()

        saveResponseDetailsq10 = ResponseDetail(summary=summaryObj, question=questionObj10, score=int(saveform1_score_10))
        saveResponseDetailsq10.save()

        saveResponseDetailsq11 = ResponseDetail(summary=summaryObj, question=questionObj11, score=int(saveform1_score_11))
        saveResponseDetailsq11.save()

        saveResponseDetailsq12 = ResponseDetail(summary=summaryObj, question=questionObj12, score=int(saveform1_score_12))
        saveResponseDetailsq12.save()

        saveResponseDetailsq13 = ResponseDetail(summary=summaryObj, question=questionObj13, score=int(saveform1_score_13))
        saveResponseDetailsq13.save()

        saveResponseDetailsq14 = ResponseDetail(summary=summaryObj, question=questionObj14, score=int(saveform1_score_14))
        saveResponseDetailsq14.save()

        saveResponseDetailsq15 = ResponseDetail(summary=summaryObj, question=questionObj15, score=int(saveform1_score_15))
        saveResponseDetailsq15.save()

        saveResponseDetailsq16 = ResponseDetail(summary=summaryObj, question=questionObj16, score=int(saveform1_score_16))
        saveResponseDetailsq16.save()

    if form2:

        getpk = ResponseSummary.objects.latest('summary_id')._get_pk_val()
        summaryObj = ResponseSummary.objects.get(summary_id=getpk)

        saveResponseDetailsq17 = ResponseDetail(summary=summaryObj, question=questionObj17, score=int(saveform2_score_17))
        saveResponseDetailsq17.save()

        saveResponseDetailsq18 = ResponseDetail(summary=summaryObj, question=questionObj18, score=int(saveform2_score_18))
        saveResponseDetailsq18.save()

        saveResponseDetailsq19 = ResponseDetail(summary=summaryObj, question=questionObj19, score=int(saveform2_score_19))
        saveResponseDetailsq19.save()

        saveResponseDetailsq20 = ResponseDetail(summary=summaryObj, question=questionObj20, score=int(saveform2_score_20))
        saveResponseDetailsq20.save()

        saveResponseDetailsq21 = ResponseDetail(summary=summaryObj, question=questionObj21, score=int(saveform2_score_21))
        saveResponseDetailsq21.save()

        saveResponseDetailsq22 = ResponseDetail(summary=summaryObj, question=questionObj22, score=int(saveform2_score_22))
        saveResponseDetailsq22.save()

        saveResponseDetailsq23 = ResponseDetail(summary=summaryObj, question=questionObj23, score=int(saveform2_score_23))
        saveResponseDetailsq23.save()

        saveResponseDetailsq24 = ResponseDetail(summary=summaryObj, question=questionObj24, score=int(saveform2_score_24))
        saveResponseDetailsq24.save()

        saveResponseDetailsq25 = ResponseDetail(summary=summaryObj, question=questionObj25, score=int(saveform2_score_25))
        saveResponseDetailsq25.save()

        saveResponseDetailsq26 = ResponseDetail(summary=summaryObj, question=questionObj26, score=int(saveform2_score_26))
        saveResponseDetailsq26.save()

        saveResponseDetailsq27 = ResponseDetail(summary=summaryObj, question=questionObj27, score=int(saveform2_score_27))
        saveResponseDetailsq27.save()

        saveResponseDetailsq28 = ResponseDetail(summary=summaryObj, question=questionObj28, score=int(saveform2_score_28))
        saveResponseDetailsq28.save()

        saveResponseDetailsq29 = ResponseDetail(summary=summaryObj, question=questionObj29, score=int(saveform2_score_29))
        saveResponseDetailsq29.save()

        saveResponseDetailsq30 = ResponseDetail(summary=summaryObj, question=questionObj30, score=int(saveform2_score_30))
        saveResponseDetailsq30.save()

    if form3:

        getpk = ResponseSummary.objects.latest('summary_id')._get_pk_val()
        summaryObj = ResponseSummary.objects.get(summary_id=getpk)

        saveResponseDetailsq31 = ResponseDetail(summary=summaryObj, question=questionObj31, score=int(saveform3_score_31))
        saveResponseDetailsq31.save()

        saveResponseDetailsq32 = ResponseDetail(summary=summaryObj, question=questionObj32, score=int(saveform3_score_32))
        saveResponseDetailsq32.save()

        saveResponseDetailsq33 = ResponseDetail(summary=summaryObj, question=questionObj33, score=int(saveform3_score_33))
        saveResponseDetailsq33.save()

        saveResponseDetailsq34 = ResponseDetail(summary=summaryObj, question=questionObj34, score=int(saveform3_score_34))
        saveResponseDetailsq34.save()

        saveResponseDetailsq35 = ResponseDetail(summary=summaryObj, question=questionObj35, score=int(saveform3_score_35))
        saveResponseDetailsq35.save()

        saveResponseDetailsq36 = ResponseDetail(summary=summaryObj, question=questionObj36, score=int(saveform3_score_36))
        saveResponseDetailsq36.save()

        saveResponseDetailsq37 = ResponseDetail(summary=summaryObj, question=questionObj37, score=int(saveform3_score_37))
        saveResponseDetailsq37.save()

        saveResponseDetailsq38 = ResponseDetail(summary=summaryObj, question=questionObj38, score=int(saveform3_score_38))
        saveResponseDetailsq38.save()

    if form4:

        getpk = ResponseSummary.objects.latest('summary_id')._get_pk_val()
        summaryObj = ResponseSummary.objects.get(summary_id=getpk)

        saveResponseDetailsq39 = ResponseDetail(summary=summaryObj, question=questionObj39, score=int(saveform4_score_39))
        saveResponseDetailsq39.save()

        saveResponseDetailsq40 = ResponseDetail(summary=summaryObj, question=questionObj40, score=int(saveform4_score_40))
        saveResponseDetailsq40.save()

        saveResponseDetailsq41 = ResponseDetail(summary=summaryObj, question=questionObj41, score=int(saveform4_score_41))
        saveResponseDetailsq41.save()

        saveResponseDetailsq42 = ResponseDetail(summary=summaryObj, question=questionObj42, score=int(saveform4_score_42))
        saveResponseDetailsq42.save()

        saveResponseDetailsq43 = ResponseDetail(summary=summaryObj, question=questionObj43, score=int(saveform4_score_43))
        saveResponseDetailsq43.save()

        saveResponseDetailsq44 = ResponseDetail(summary=summaryObj, question=questionObj44, score=int(saveform4_score_44))
        saveResponseDetailsq44.save()

        saveResponseDetailsq45 = ResponseDetail(summary=summaryObj, question=questionObj45, score=int(saveform4_score_45))
        saveResponseDetailsq45.save()

        saveResponseDetailsq46 = ResponseDetail(summary=summaryObj, question=questionObj46, score=int(saveform4_score_46))
        saveResponseDetailsq46.save()

    if form5:

        getpk = ResponseSummary.objects.latest('summary_id')._get_pk_val()
        summaryObj = ResponseSummary.objects.get(summary_id=getpk)

        saveResponseDetailsq47 = ResponseDetail(summary=summaryObj, question=questionObj47, score=int(saveform5_score_47))
        saveResponseDetailsq47.save()

        saveResponseDetailsq48 = ResponseDetail(summary=summaryObj, question=questionObj48, score=int(saveform5_score_48))
        saveResponseDetailsq48.save()

        saveResponseDetailsq49 = ResponseDetail(summary=summaryObj, question=questionObj49, score=int(saveform5_score_49))
        saveResponseDetailsq49.save()

        saveResponseDetailsq50 = ResponseDetail(summary=summaryObj, question=questionObj50, score=int(saveform5_score_50))
        saveResponseDetailsq50.save()

        saveResponseDetailsq51 = ResponseDetail(summary=summaryObj, question=questionObj51, score=int(saveform5_score_51))
        saveResponseDetailsq51.save()




    #msg= "Successfully Assessment completed by: " + str(saveform1_username) + " on " + str(saveform1_assessmentDate) + " for " + str(saveform1_siteCode) + " , " + str(saveform1_assessment.assessmentName) + " : " + str(saveform1_period)
    # variables= RequestContext(self.request,{'msg': msg})
    # return render_to_response('assessment/done.html', variables)
    return form_data