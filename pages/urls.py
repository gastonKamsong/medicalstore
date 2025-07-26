from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('legal/', views.legal, name='legal'),
    path('privacy/', views.privacy, name='privacy'),
    path('services/', views.services, name='services'),
    path('shipping/', views.shipping, name='shipping'),
    path('returns_policy/', views.returns_policy, name='returns_policy'),
]