from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^defect_notice/', include('defect_notice.urls')), # Add this tuple to include app urls
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^assessment/', include('assessment.urls')),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
