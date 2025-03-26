from django.urls import path
from . import views

urlpatterns = [
    path('', views.learnmore, name='learnmore'),  # Root URL now goes to learnmore
    path('waitlist/', views.home, name='home'),
    path('community/', views.community, name='community')
]
