from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('collections/', views.collections_index, name='index'),
    path('collections/<int:collection_id>/', views.collections_detail, name='detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
]