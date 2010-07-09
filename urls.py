from django.conf.urls.defaults import *
from django.conf import settings
from settings import absolute
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lanmpd/', include('lanmpd.foo.urls')),
    (r'^web/$', 'lanmpd.web.views.index'),
    (r'^web/login/$', 'django.contrib.auth.views.login', {'template_name': absolute('templates/auth.html')}),
    (r'^web/logout/$', 'lanmpd.web.views.unauth'),
    (r'^web/player/$', 'lanmpd.web.views.player'),
    (r'^web/player/change_song/$', 'lanmpd.web.views.change_song'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    (r'^admin/$', include(admin.site.urls))
)

if settings.DEVELOPMENT:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': settings.MEDIA_ROOT}))

