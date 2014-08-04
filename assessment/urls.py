__author__ = 'anithrao'
import os
from django.conf.urls import patterns, include, url
from defect_notice import models
from views import *
from forms import *
from models import *
from django.views.static import serve



js = os.path.join(os.path.dirname(__file__), 'js')
css = os.path.join(os.path.dirname(__file__), 'css')
images = os.path.join(os.path.dirname(__file__), 'images')


urlpatterns = patterns('',
    # url(r'^monthly/$', MonthlyAssessmentWizard.as_view([MonthlyAssessForm1,MonthlyAssessForm2])),
    # url(r'^monthly/name=saveform1$', saveform1),
    url(r'^monthly/$', MonthlyAssessmentWizard.as_view([MonthlyAssessForm1,MonthlyAssessForm2,MonthlyAssessForm3,MonthlyAssessForm4,MonthlyAssessForm5])),
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


        # site media
    (r'^javascripts/(?P<path>.*)$', serve,
     {'document_root': js}),

    # stylesheets
    (r'^stylesheets/(?P<path>.*)$', serve,
     {'document_root': css}),

    # images
    (r'^images/(?P<path>.*)$', serve,
     {'document_root': images}),

)