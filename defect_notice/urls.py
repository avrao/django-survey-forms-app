import os
from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView



js = os.path.join(os.path.dirname(__file__), 'js')
css = os.path.join(os.path.dirname(__file__), 'css')
images = os.path.join(os.path.dirname(__file__), 'images')


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^test$', test),
    url(r'^about$', TemplateView.as_view(template_name='defect_notice/about.html')),
    url(r'^add$', add),
    url(r'^search$', search),
    url(r'^report$', report_defectnotice),
	url(r'^report?page=[\d]$', report_defectnotice),
    url(r'^approve$', approve),
    url(r'^render_pdf/(?P<id>.*)$', pdfserve_fdn),
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),

    # site media
    (r'^js/(?P<path>.*)$', serve,
    {'document_root': js}),

    # stylesheets
    (r'^stylesheets/(?P<path>.*)$', serve,
    {'document_root': css}),

    # images
    (r'^images/(?P<path>.*)$', serve,
    {'document_root': images}),

)

