from django.urls import path
from . import views
from .views import BaseView, AboutView, AnketsView, JAnketsView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/main/', permanent=True), name='core'),
    path('main/', BaseView.as_view()),
    path('form/', AboutView.as_view()),
    path('ankets/', AnketsView.as_view(), name='ankets'),
    path('get_data/', JAnketsView.as_view(), name='get_data'),
]