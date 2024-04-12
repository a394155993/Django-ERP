# from django.conf.urls import include, url,static
# import invent.views
#
# urlpatterns = [
#     url(r"stockin/(?P<object_id>\d+)/cin", invent.views.action_in),
#     url(r"initialinventory/(?P<object_id>\d+)/cin", invent.views.action_init),
#     url(r"stockout/(?P<object_id>\d+)/out", invent.views.action_out),
#     url(r"warereturn/(?P<object_id>\d+)/cin", invent.views.action_return),
#     url(r"wareadjust/(?P<object_id>\d+)/adjust", invent.views.action_adjust),
# ]
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
import invent.views

urlpatterns = [
    re_path(r"stockin/(?P<object_id>\d+)/cin$", invent.views.action_in),
    re_path(r"initialinventory/(?P<object_id>\d+)/cin$", invent.views.action_init),
    re_path(r"stockout/(?P<object_id>\d+)/out$", invent.views.action_out),
    re_path(r"warereturn/(?P<object_id>\d+)/cin$", invent.views.action_return),
    re_path(r"wareadjust/(?P<object_id>\d+)/adjust$", invent.views.action_adjust),
]

# Optionally handle static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
