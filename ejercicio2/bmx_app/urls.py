from django.urls import path
from . import views

urlpatterns = [
    path('', views.DateRangeView.as_view(), name='select_date_range'),
    path('data/<str:serie>/<str:fechaInicial>/<str:fechaFinal>/',
         views.DataView.as_view(), name='data'),
]
