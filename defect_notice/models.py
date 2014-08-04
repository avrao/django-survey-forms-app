from datetime import date
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError

# Create your models here.

class SiteDetailsLookup(models.Model):
    siteCode = models.CharField(max_length=45)

    def __unicode__(self):
        return self.siteCode
    class Meta:
        db_table = 'siteDetailsLookup'

class InfrastructureDivisionLookup(models.Model):
    divisionAsset = models.CharField(max_length=128)

    def __unicode__(self):
        return self.divisionAsset
    class Meta:
        db_table = 'infrastructureDivisionLookup'

class InfrastructureSystemLookup(models.Model):
    systemAsset = models.CharField(max_length=128)

    def __unicode__(self):
        return self.systemAsset
    class Meta:
        db_table = 'infrastructureSystemLookup'

class DefectSourceLookup(models.Model):
    defectSource = models.CharField(max_length=128)

    def __unicode__(self):
        return unicode(self.defectSource)
    class Meta:
        db_table = 'defectSourceLookup'

class DefectDetails(models.Model):
    username = models.CharField(max_length=250,null=False)
    #siteCode_id = models.ForeignKey(SiteDetailsLookup)
    site = models.CharField(max_length=250,null=False)
    ttnumber = models.CharField(max_length=250,null=True)
    infrastructureDivision_id = models.ForeignKey(InfrastructureDivisionLookup)
    infrastructureSystem_id = models.ForeignKey(InfrastructureSystemLookup)
    infrastructureSubsystem = models.CharField(max_length=250,null=True)
    incidentDate = models.DateField(auto_now=False)
    defectSource_id = models.ForeignKey(DefectSourceLookup)
    critical = models.BooleanField(choices=((1, 'Yes'), (0, 'No')))
    largeScale = models.BooleanField(choices=((1, 'Yes'), (0, 'No')))
    assetManufacturer = models.CharField(max_length=250,null=True)
    assetModelNumber = models.CharField(max_length=250,null=True)
    referenceFile = models.FileField(upload_to='FDN/', null=True)
    filename = models.CharField(max_length=250,null=True)
    defectSynopsis = models.TextField(null=True)
    notifierEmail = models.EmailField(max_length=250,null=False)
    approved = models.BooleanField(choices=((1, 'Yes'), (0, 'No')))
    approvalDate = models.DateField(auto_now=False)

    def getdefectDetails_id(self):
            return self.defectDetails_id

    def getinfrastructureSubsystem(self):
        return self.infrastructureSubsystem

    def getassetManufacturer(self):
        return self.assetManufacturer

    def getassetModelNumber(self):
        return self.assetModelNumber

    def getdefectSynopsis(self):
        return self.defectSynopsis

    def getsites(self):
        return self.site

    def getusername(self):
        return self.username

    def getdivision(self):
        return self.divisionAsset

    def getsystem(self):
        return self.systemAsset

    def getdefectsource(self):
        return self.defectSource

    def getapproved(self):
        return self.approved

    class Meta:
        db_table = 'defectDetails'
