from django.conf.urls.defaults import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'WebMonitor.views.home', name='home'),
    # url(r'^WebMonitor/', include('WebMonitor.foo.urls')),
	# other commented code here
	#(r'^admin/', include(admin.site.urls)),

	#(r'^accounts/', include('django.contrib.auth.urls')),

	(r'^monitor/$', 'WebMonitor.views.indexView',{'template_name': 'index.html'}, 'index'),
)
