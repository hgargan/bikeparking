from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bikeparking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'parking.views.home', name='home'),
    url(r'^find/', 'parking.views.find', name='find'),
    url(r'^detail/(?P<pk>\d+)$', 'parking.views.detail', name='detail'),
    url(r'^review/', 'parking.views.review', name='review'),
    url(r'^submit/', 'parking.views.submit', name='submit')
)
