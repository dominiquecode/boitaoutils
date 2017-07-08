from django.conf.urls import url
from . import views as photos_views

urlpatterns = [
    url(r'^$', photos_views.home, name='home'),

]