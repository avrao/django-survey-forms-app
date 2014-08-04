from django.contrib import admin
from defect_notice.models import SiteDetailsLookup, InfrastructureDivisionLookup, InfrastructureSystemLookup, DefectSourceLookup, DefectDetails



#Register your models here.
admin.site.register(SiteDetailsLookup)
admin.site.register(InfrastructureDivisionLookup)
admin.site.register(InfrastructureSystemLookup)
admin.site.register(DefectSourceLookup)
admin.site.register(DefectDetails)





