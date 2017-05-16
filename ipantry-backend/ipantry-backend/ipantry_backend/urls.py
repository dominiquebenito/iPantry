"""
Definition of urls for ipantry_backend.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ipantry_backend.views.home, name='home'),
    # url(r'^ipantry_backend/', include('ipantry_backend.ipantry_backend.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # API url
    url(r'api/', include('api.urls'))
]
