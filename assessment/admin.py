from django.contrib import admin
from models import *
from defect_notice.models import SiteDetailsLookup

#Register your models here.
admin.site.register(Assessment)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(ResponseDetail)
admin.site.register(ResponseSummary)

