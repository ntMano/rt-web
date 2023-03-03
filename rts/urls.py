from django.urls import path
from . import views
urlpatterns = [
    path('', views.rts, name="rts" ),
    path('att_rt/', views.att_rt, name="att_rt" )


]