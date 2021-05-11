from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('account/', views.Account.as_view(), name='account'),
    path('wishlist/', views.Wishlist.as_view(), name='wishlist'),
    path('about/', views.About.as_view(), name='about'),
    path('filter/', views.FilterSeedView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('catalog/<slug:slug>/', views.SeedDetail.as_view(), name='seed_detail'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('faqs/', views.Faqs.as_view(), name='faqs'),
]
