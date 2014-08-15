from django.contrib import admin as django_admin

from mymcadmin.core import models as app_models

django_admin.site.register(app_models.Server)

