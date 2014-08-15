from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mymcadmin.core import views as app_views

from ynot.django.auth import views as auth_views

urlpatterns = patterns('',
	url(
		r'^$',
		app_views.HomeView.as_view(),
		name = 'root',
	),
	url(
		r'^login$',
		auth_views.LoginView.as_view(),
		name = 'login',
	),
	url(
		r'^logout$',
		auth_views.LogoutView.as_view(),
		name = 'logout',
	),
	url(
		r'^server/(?P<pk>\d+)$',
		app_views.ServerDetailView.as_view(),
		name = 'server-view'
	),

    url(
		r'^admin/', include(admin.site.urls)
	),
)

