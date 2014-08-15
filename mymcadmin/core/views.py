from django.views import generic as django_views

from mymcadmin.core import models as app_models

from ynot.django.auth import views as ynot_views

class HomeView(ynot_views.LoginRequiredMixin, django_views.TemplateView):
	template_name = 'home.html'

class ServerDetailView(ynot_views.LoginRequiredMixin, django_views.DetailView):
	model         = app_models.Server
	template_name = 'server/view.html'

