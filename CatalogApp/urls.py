from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('filter/', views.FilterSeedView.as_view(), name='filter'),
    path('catalog/<slug:slug>/', views.SeedDetail.as_view(), name='seed_detail'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('faqs/', views.Faqs.as_view(), name='faqs'),
]
