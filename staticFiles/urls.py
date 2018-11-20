from django.conf.urls import url
from django.contrib import admin
from testApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^profile/', views.profile),
]
