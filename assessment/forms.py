__author__ = 'anithrao'
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from defect_notice.models import *
from models import *
from datetime import date
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        internal=''.join(['<span id="radio">%s</span>' % w for w in self])
        return mark_safe(u'%s' %internal)

class MonthlyAssessForm1(forms.Form):
    def __init__(self, *args, **kwargs):
        # This should be done before any references to self.fields
        super(MonthlyAssessForm1, self).__init__(*args, **kwargs)


        catObj=Category.objects.get(assessment_id=1, categoryPosition=1)
        singlecategory = catObj.category_id
        questions = Question.objects.filter(category_id=singlecategory)
        qlist=[]

        for i in questions.iterator():
            qlist.append(i.question_id)

        self.questions = questions
        self.id_list = []
        # Some generic loop condition to create the fields
        for i in questions:

            #self.id_list.append(i.question_id)

            # Create and add the field to the form
            field = forms.TypedChoiceField(widget=forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')],
                                      error_messages={'required': 'Please select a score'})
            self.fields["score_%s" % i.question_id] = field
            self.id_list.append(field)

            field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-1])
            self.fields["question_id%s" % i.question_id] = field

    catObj=Category.objects.get(assessment_id=1, categoryPosition=1)
    catname=catObj.categoryName
    title = catObj.assessment.assessmentName
    singlecategory = catObj.category_id
    questions = Question.objects.filter(category_id=singlecategory)

    username = forms.CharField(max_length=60, label='User Name',error_messages={'required': 'Please enter your User Name'})
    siteCode = forms.ModelChoiceField(SiteDetailsLookup.objects.all(),label='Site', empty_label=None)
    assessmentDate = forms.DateField(label="Date", required=True, input_formats=['%m-%d-%Y'],initial=date.today().strftime('%m-%d-%Y'),
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        help_text="Format: MM-DD-YYYY",error_messages={'required': 'Please pick a date'})
    period = forms.CharField(widget=forms.HiddenInput(), initial='Monthly: ' + date.today().strftime('%m-%Y'))
    assessment_id = forms.CharField(widget=forms.HiddenInput(),initial=catObj.assessment.assessment_id, required=False)

class MonthlyAssessForm2(forms.Form):
    def __init__(self, *args, **kwargs):
        # This should be done before any references to self.fields
        super(MonthlyAssessForm2, self).__init__(*args, **kwargs)

        catObj=Category.objects.get(assessment_id=1, categoryPosition=2)
        singlecategory = catObj.category_id

        questions = Question.objects.filter(category_id=singlecategory)
        qlist=[]
        for i in questions.iterator():
            qlist.append(i.question_id)
        print qlist
        self.questions = questions
        #self.id_list = []

        # Some generic loop condition to create the fields
        for i in questions:

            #self.id_list.append(i.question_id)

            # Create and add the field to the form
            field = forms.TypedChoiceField(widget = forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer), error_messages={'required': 'Please select a score'}, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')])
            self.fields["score_%s" % i.question_id] = field

            #Here qlst[17,18]. initial=qlist[i.question_id-17] - get the question_id number and subtract by the first item from the list.
            field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-17])
            self.fields["question_id%s" % i.question_id] = field
    catObj=Category.objects.get(assessment_id=1, categoryPosition=2)
    catname=catObj.categoryName
    title = catObj.assessment.assessmentName
    singlecategory = catObj.category_id
class MonthlyAssessForm3(forms.Form):
    def __init__(self, *args, **kwargs):
        # This should be done before any references to self.fields
        super(MonthlyAssessForm3, self).__init__(*args, **kwargs)

        catObj=Category.objects.get(assessment_id=1, categoryPosition=3)
        singlecategory = catObj.category_id

        questions = Question.objects.filter(category_id=singlecategory)
        qlist=[]
        for i in questions.iterator():
            qlist.append(i.question_id)
        print qlist
        self.questions = questions
        #self.id_list = []

        # Some generic loop condition to create the fields
        for i in questions:

            #self.id_list.append(i.question_id)

            # Create and add the field to the form
            field = forms.TypedChoiceField(widget = forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer), error_messages={'required': 'Please select a score'}, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')])
            self.fields["score_%s" % i.question_id] = field

            #Here qlst[17,18]. initial=qlist[i.question_id-17] - get the question_id number and subtract by the first item from the list.
            field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-31])
            self.fields["question_id%s" % i.question_id] = field
    catObj=Category.objects.get(assessment_id=1, categoryPosition=3)
    catname=catObj.categoryName
    title = catObj.assessment.assessmentName
    singlecategory = catObj.category_id

class MonthlyAssessForm4(forms.Form):
    def __init__(self, *args, **kwargs):
        # This should be done before any references to self.fields
        super(MonthlyAssessForm4, self).__init__(*args, **kwargs)

        catObj=Category.objects.get(assessment_id=1, categoryPosition=4)
        singlecategory = catObj.category_id

        questions = Question.objects.filter(category_id=singlecategory)
        qlist=[]
        for i in questions.iterator():
            qlist.append(i.question_id)
        print qlist
        self.questions = questions
        #self.id_list = []

        # Some generic loop condition to create the fields
        for i in questions:

            #self.id_list.append(i.question_id)

            # Create and add the field to the form
            field = forms.TypedChoiceField(widget = forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer), error_messages={'required': 'Please select a score'}, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')])
            self.fields["score_%s" % i.question_id] = field

            #Here qlst[17,18]. initial=qlist[i.question_id-17] - get the question_id number and subtract by the first item from the list.
            field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-39])
            self.fields["question_id%s" % i.question_id] = field
    catObj=Category.objects.get(assessment_id=1, categoryPosition=4)
    catname=catObj.categoryName
    title = catObj.assessment.assessmentName
    singlecategory = catObj.category_id

class MonthlyAssessForm5(forms.Form):
    def __init__(self, *args, **kwargs):
            # This should be done before any references to self.fields
            super(MonthlyAssessForm5, self).__init__(*args, **kwargs)

            catObj=Category.objects.get(assessment_id=1, categoryPosition=5)
            singlecategory = catObj.category_id

            questions = Question.objects.filter(category_id=singlecategory)
            qlist=[]
            for i in questions.iterator():
                qlist.append(i.question_id)
            print qlist
            self.questions = questions
            #self.id_list = []

            # Some generic loop condition to create the fields
            for i in questions:

                #self.id_list.append(i.question_id)

                # Create and add the field to the form
                field = forms.TypedChoiceField(widget = forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer), error_messages={'required': 'Please select a score'}, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')])
                self.fields["score_%s" % i.question_id] = field

                #Here qlst[17,18]. initial=qlist[i.question_id-17] - get the question_id number and subtract by the first item from the list.
                field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-47])
                self.fields["question_id%s" % i.question_id] = field

    catObj=Category.objects.get(assessment_id=1, categoryPosition=5)
    catname=catObj.categoryName
    title = catObj.assessment.assessmentName
    singlecategory = catObj.category_id



# __author__ = 'anithrao'
# from django import forms
# from django.core import validators
# from django.core.exceptions import ValidationError
# from defect_notice.models import *
# from models import *
# from datetime import date
# from django.forms.widgets import RadioSelect
# from django.utils.safestring import mark_safe
#
# class HorizontalRadioRenderer(RadioSelect.renderer):
#     def render(self):
#         internal=''.join(['<span id="radio">%s</span>' % w for w in self])
#         return mark_safe(u'%s' %internal)
#     # def render(self):
#     #     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
#
# class MonthlyAssessForm1(forms.Form):
#     def __init__(self, *args, **kwargs):
#         # This should be done before any references to self.fields
#         super(MonthlyAssessForm1, self).__init__(*args, **kwargs)
#
#
#         catObj=Category.objects.get(assessment_id=1, categoryPosition=1)
#         catname=catObj.categoryName
#         singlecategory = catObj.category_id
#         questions = Question.objects.filter(category_id=singlecategory)
#         qlist=[]
#
#         for i in questions.iterator():
#             qlist.append(i.question_id)
#
#         self.questions = questions
#         self.id_list = []
#         # Some generic loop condition to create the fields
#         for i in questions:
#
#             #self.id_list.append(i.question_id)
#
#             # Create and add the field to the form
#             field = forms.TypedChoiceField(widget=forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer),
#                                       choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')],
#                                       error_messages={'required': 'Please select a score'})
#             self.fields["score_%s" % i.question_id] = field
#             self.id_list.append(field)
#
#             field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-1])
#             self.fields["question_id%s" % i.question_id] = field
#
#     catObj=Category.objects.get(assessment_id=1, categoryPosition=1)
#     catname=catObj.categoryName
#     title = catObj.assessment.assessmentName
#     singlecategory = catObj.category_id
#     questions = Question.objects.filter(category_id=singlecategory)
#
#     username = forms.CharField(max_length=60, label='User Name',error_messages={'required': 'Please enter your User Name'})
#     siteCode = forms.ModelChoiceField(SiteDetailsLookup.objects.all(),label='Site', empty_label=None)
#     assessmentDate = forms.DateField(label="Date", required=True, input_formats=['%m-%d-%Y'],initial=date.today().strftime('%m-%d-%Y'),
#         widget=forms.DateInput(attrs={'class': 'datepicker'}),
#         help_text="Format: MM-DD-YYYY",error_messages={'required': 'Please pick a date'})
#     period = forms.CharField(widget=forms.HiddenInput(), initial='Monthly: ' + date.today().strftime('%m-%Y'))
#     assessment_id = forms.CharField(widget=forms.HiddenInput(),initial=catObj.assessment.assessment_id, required=False)
#
#         # Change the field options
#         #self.fields['choice_field'].widget.choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')]
#
#     # qlist=[]
#     # for i in questions.iterator():
#     #     qlist.append(i.question_id)
#
#     # hiddenValues = forms.Form()
#     # value0 = qlist[i.question_id-1]
#     #
#     # hiddenValues.fields['questionid_'] = forms.CharField(initial=value0,
#     # widget=forms.widgets.HiddenInput())
#
#     # username = forms.CharField(max_length=60, label='User Name',error_messages={'required': 'Please enter your User Name'})
#     # siteCode = forms.ModelChoiceField(SiteDetailsLookup.objects.all(),label='Site', empty_label=None)
#     # assessmentDate = forms.DateField(label="Date", required=True, input_formats=['%m-%d-%Y'],initial=date.today().strftime('%m-%d-%Y'),
#     #     widget=forms.DateInput(attrs={'class': 'datepicker'}),
#     #     help_text="Format: MM-DD-YYYY",error_messages={'required': 'Please pick a date'})
#     # question_id1 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[0], required=False)
#     # question_id2 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[1], required=False)
#     # question_id3 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[2], required=False)
#     # question_id4 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[3], required=False)
#     # question_id5 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[4], required=False)
#     # question_id6 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[5], required=False)
#     # question_id7 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[6], required=False)
#     # question_id8 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[7], required=False)
#     # question_id9 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[8], required=False)
#     # question_id10 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[9], required=False)
#     # question_id11 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[10], required=False)
#     # question_id12 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[11], required=False)
#     # question_id13 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[12], required=False)
#     # question_id14 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[13], required=False)
#     # question_id15 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[14], required=False)
#     # question_id16 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[15], required=False)
#
#     # period = forms.CharField(widget=forms.HiddenInput(), initial='Monthly: ' + date.today().strftime('%m-%Y'))
#     #
#     # assessment_id = forms.CharField(widget=forms.HiddenInput(),initial=catObj.assessment.assessment_id, required=False)
#
#     # score1 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score2 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score3 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score4 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score5 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score6 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score7 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score8 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score9 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score10 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score11 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score12 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score13 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score14 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#     # score15 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score16 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')), error_messages={'required': 'Please select a score'})
#
# class MonthlyAssessForm2(forms.Form):
#     # catObj=Category.objects.get(assessment_id=1, categoryPosition=2)
#     # catname=catObj.categoryName
#     # title = catObj.assessment.assessmentName
#     # singlecategory = catObj.category_id
#     #
#     # questions = Question.objects.filter(category_id=singlecategory)
#     # qlist=[]
#     # for i in questions.iterator():
#     #     qlist.append(i.question_id)
#
#     def __init__(self, *args, **kwargs):
#         # This should be done before any references to self.fields
#         super(MonthlyAssessForm2, self).__init__(*args, **kwargs)
#
#         catObj=Category.objects.get(assessment_id=1, categoryPosition=2)
#         singlecategory = catObj.category_id
#
#         questions = Question.objects.filter(category_id=singlecategory)
#         qlist=[]
#         for i in questions.iterator():
#             qlist.append(i.question_id)
#         print qlist
#         self.questions = questions
#         #self.id_list = []
#
#         # Some generic loop condition to create the fields
#         for i in questions:
#
#             #self.id_list.append(i.question_id)
#
#             # Create and add the field to the form
#             field = forms.TypedChoiceField(widget = forms.widgets.RadioSelect(renderer=HorizontalRadioRenderer), error_messages={'required': 'Please select a score'}, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'n/a')])
#             self.fields["score_%s" % i.question_id] = field
#
#             #Here qlst[17,18]. initial=qlist[i.question_id-17] - get the question_id number and subtract by the first item from the list.
#             field = forms.CharField(widget=forms.HiddenInput(),initial=qlist[i.question_id-17])
#             self.fields["question_id%s" % i.question_id] = field
#
#
#     #radio_ids = [ i+1 for i in range(6)]
#
#     # question_id21 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[0], required=False)
#     # question_id22 = forms.CharField(widget=forms.HiddenInput(),initial=qlist[1], required=False)
#     # score21 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (2, 'n/a')), error_messages={'required': 'Please select a score'})
#     # score22 = forms.TypedChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (2, 'n/a')), error_messages={'required': 'Please select a score'})
#     #
#
# # class MonthlyAssessForm3(forms.Form):
# #     catObj=Category.objects.get(assessment_id=1, categoryPosition=3)
# #     catname=catObj.categoryName
# #     title = catObj.assessment.assessmentName
# #     singlecategory = catObj.category_id
# #
# #     questions = Question.objects.filter(category_id=singlecategory)
# #     radio_ids = [ i+1 for i in range(6)]
# #
# # class MonthlyAssessForm4(forms.Form):
# #     catObj=Category.objects.get(assessment_id=1, categoryPosition=4)
# #     catname=catObj.categoryName
# #     title = catObj.assessment.assessmentName
# #     singlecategory = catObj.category_id
# #
# #     questions = Question.objects.filter(category_id=singlecategory)
# #     radio_ids = [ i+1 for i in range(6)]
# #
# # class MonthlyAssessForm5(forms.Form):
# #     catObj=Category.objects.get(assessment_id=1, categoryPosition=5)
# #     catname=catObj.categoryName
# #     title = catObj.assessment.assessmentName
# #     singlecategory = catObj.category_id
# #
# #     questions = Question.objects.filter(category_id=singlecategory)
# #     radio_ids = [ i+1 for i in range(6)]
#
