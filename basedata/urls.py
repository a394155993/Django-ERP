# from django.conf.urls import include, url,static
# import basedata.views
#
# urlpatterns = [
#     url(r"dataimport/(?P<object_id>\d+)/action", basedata.views.action_import),
# ]
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
import basedata.views

urlpatterns = [
    re_path(r"dataimport/(?P<object_id>\d+)/action$", basedata.views.action_import),
]

# 在开发环境中添加静态和媒体文件的处理
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
