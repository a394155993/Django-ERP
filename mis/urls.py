from django.urls import include, re_path, path
from django.contrib import admin
from mis import settings
import workflow.views
import invent.urls
import basedata.urls
import selfhelp.urls
import mis.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', mis.views.home),
    re_path(r'^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start$', workflow.views.start),
    re_path(r'^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)$',
            workflow.views.approve),
    re_path(r'^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)$',
            workflow.views.restart),
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^admin/invent/', include(invent.urls)),
    re_path(r'^admin/basedata/', include(basedata.urls)),
    re_path(r'^admin/selfhelp/', include(selfhelp.urls)),
]

# 在开发环境中添加静态和媒体文件的处理
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
