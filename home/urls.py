from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact_confirmation/', views.contact, name='contact_confirmation'),
    path('about_us/', views.aboutUs, name='about us'),
    path('learn/', views.learn, name='learn'),
    path('endometriosis/', views.endometriosis, name='endometriosis'),
    path('menopause/', views.menopause, name='menopause'),
    path('not_being_heard/', views.notBeingHeard, name='Not being heard'),
]
