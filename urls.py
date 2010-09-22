from django.conf.urls.defaults import *
from view import option, index, textarea
import os.path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    ("^/?$", index),
    ("^option/(\w+)/(\w+)/$", option),
    ("^text/$", textarea),    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/rex/git/dregex/media'}),
    
    # Example:
    # (r'^dregex/', include('dregex.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
