__author__ = 'anithrao'
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from defect_notice.models import *
from datetime import date

#class ContactForm(forms.Form):
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField()
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)

class DefectForm(forms.Form):
    # user_name = forms.ModelChoiceField(LoginLookup.objects.all(),error_messages={'required': 'Please select User ID'},empty_label=None)
    site_multi = forms.ModelMultipleChoiceField(SiteDetailsLookup.objects.all(),label='Site Code',error_messages={'required': 'Please select one or more Site Code/s'})
    tt_number = forms.CharField(max_length=128, label='Trouble Ticket Number', required=False)
    incident_date = forms.DateField(label="Incident Date", required=True, input_formats=['%m-%d-%Y'],initial=date.today().strftime('%m-%d-%Y'),
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        help_text="Format: MM-DD-YYYY",error_messages={'required': 'Please pick a date'})
    indicator_source = forms.ModelChoiceField(DefectSourceLookup.objects.all(), empty_label=None,label="Source of First Indication", error_messages={'required': 'Please provide source of the defect.'})
    critical_load = forms.TypedChoiceField(label="Critical Load Loss", widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')),initial=0, error_messages={'required': 'Please select severity of load'})
    large_scale = forms.TypedChoiceField(label="Large Scale Event", widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')),initial=0, error_messages={'required': 'Please select scale of defect'})
    division_asset = forms.ModelChoiceField(InfrastructureDivisionLookup.objects.all(), empty_label=None,label="Infrastructure Division")
    system_asset = forms.ModelChoiceField(InfrastructureSystemLookup.objects.all(), empty_label=None, label="Infrastructure System")
    subsystem_asset = forms.CharField(label="Infrastructure Subsystem", max_length=128,error_messages={'required': 'Please select Subsystem asset' })
    manufacturer_asset = forms.CharField(label="Manufacturer", max_length=128, error_messages={'required': 'Please add manufacturer asset'})
    model_number = forms.CharField(label="Model Number", max_length=128)
    referenceFile = forms.FileField(label='Reference File Upload', help_text='max 50 MB', initial='none')
    filename = forms.CharField(widget=forms.HiddenInput(),initial='none')
    defect_synopsis = forms.CharField(label="Synopsis", required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    notifier_email = forms.EmailField(widget=forms.HiddenInput(), initial='anithrao@amazon.com')
    approved = forms.TypedChoiceField(widget=forms.HiddenInput(), choices=((1, 'Yes'), (0, 'No')), initial=0)
    approvalDate = forms.DateField(widget=forms.HiddenInput(), input_formats=['%m-%d-%Y'], initial=date.today().strftime('%m-%d-%Y'))


class SearchDefectForm(forms.Form):
    id = forms.IntegerField(label="Enter ID: ", min_value=1, error_messages={'required': 'Please enter Defect Id.'})
    #defectdetails = forms.ModelChoiceField(DefectDetails._get_pk_val().all, label="Enter ID: ",error_messages={'required': 'Please enter Defect Id.'})
    
    
class ApproveDefectForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    # username = forms.ModelChoiceField(LoginLookup.objects.all(),empty_label=None, label= 'User name', error_messages={'required': 'Please select User ID'})
    # site = forms.ModelMultipleChoiceField(SiteDetailsLookup.objects.all(),label='Site Code',error_messages={'required': 'Please select one or more Site Code/s'}, help_text='Select one or many Site codes')
    site = forms.CharField(max_length=250, label='Site/s', error_messages={'required': 'Please enter Site code/s'})
    ttnumber = forms.CharField(max_length=128, label='Trouble Ticket Number', required=False,)
    incidentDate = forms.DateField(label="Incident Date", required=True,input_formats=['%m-%d-%Y'],initial=date.today().strftime('%m-%d-%Y'),
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        help_text="Format: MM-DD-YYYY",error_messages={'required': 'Please pick a date' })
    defectSource_id = forms.ModelChoiceField(DefectSourceLookup.objects.all(), empty_label=None,label="Source of First Indication", initial=0, help_text="Select a source", error_messages={'required': 'Please select User ID'})
    critical = forms.TypedChoiceField(label="Critical Load Loss", widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')),initial=0, error_messages={'required': 'Please select severity of load'})
    largeScale = forms.TypedChoiceField(label="Large Scale Event", widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')),initial=0, error_messages={'required': 'Please select scale of defect'})
    infrastructureDivision_id = forms.ModelChoiceField(InfrastructureDivisionLookup.objects.all(), empty_label=None, label="Infrastructure Division", error_messages={'required': 'Please select User ID'})
    infrastructureSystem_id = forms.ModelChoiceField(InfrastructureSystemLookup.objects.all(), empty_label=None,label="Infrastructue System", error_messages={'required': 'Please select User ID'})
    infrastructureSubsystem = forms.CharField(label="Infrastructure Subsystem", max_length=128,error_messages={'required': 'Please select Subsystem asset' })
    assetManufacturer = forms.CharField(label="Manufacturer", max_length=128, error_messages={'required': 'Please add manufacturer asset'})
    assetModelNumber = forms.CharField(label="Model Number", max_length=128)
    filename = forms.CharField(max_length=250, label='File Uploaded')
    # filename = forms.URLField(max_length=250, label='File Uploaded')
    defectSynopsis = forms.CharField(label="Synopsis", required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    notifierEmail = forms.EmailField(widget=forms.HiddenInput(), initial='anithrao@amazon.com')
    username = forms.CharField(widget=forms.HiddenInput())
    approved = forms.TypedChoiceField(label="Approve", widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')), error_messages={'required': 'Please select approval'})
    approvalDate = forms.DateField(widget=forms.HiddenInput(), input_formats=['%m-%d-%Y'], initial=date.today().strftime('%m-%d-%Y'))


    
    
