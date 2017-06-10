from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^weather/$', views.weather, name='weather'),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^weather/$', views.weather, name='weather'),
    url(r'^music/$', views.music, name='music'),
    url(r'^about/$', views.about, name="about"),
    url(r'^clock_in/$', views.clock_in, name="clock_in"),
    ulr(r'^paly_music/$', views.play_music, name="play_music"),
    ulr(r'^stop_music/$', views.stop_music, name="stop_music"),
]