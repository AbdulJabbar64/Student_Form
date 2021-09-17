from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormStd.home, name='home'),
    path('data/', views.FormStd.data, name='data'),
    path('new', views.FormStd.send, name='send'),
    path('reg', views.FormStd.reg),
]