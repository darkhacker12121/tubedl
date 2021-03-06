from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from tubedl import views

admin.autodiscover()
handler500 = "tubedl.views.error500"


urlpatterns = [
    # some browsers assume favicon.ico is present in the root directory
    url(
        r"^favicon\.ico$",
        RedirectView.as_view(url="/static/img/favicon.ico", permanent=True),
    ),
    url(r"^$", views.home, name="home"),
    url(r"^error500/$", views.error500, name="error500"),
    url(r"^admin/", admin.site.urls),
    url(r"^dl/", include("videodl.urls")),
]
