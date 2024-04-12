__author__ = 'zhugl'

# created at 15-4-22
from django.apps.config import AppConfig
from django.utils.translation import gettext_lazy as _


class OrganConfig(AppConfig):
    name = 'organ'
    verbose_name = _('organization')

    def ready(self):
        from django.contrib import admin
        admin.site.site_header = 'Django-ERP'
