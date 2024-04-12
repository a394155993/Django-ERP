__author__ = 'zhugl'

# created at 15-4-22
from django.apps.config import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseDataConfig(AppConfig):
    name = 'basedata'
    verbose_name = _('BaseData')

    def ready(self):
        from django.contrib import admin
        admin.site.site_header = 'Django-ERP'
