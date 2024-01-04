from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('collections/', views.collections_index, name='index'),
    path('collections/<int:collection_id>/', views.collections_detail, name='detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
    path('collections/<int:collection_id>/notes/create/', views.NoteCreate.as_view(), name='notes_create'),
    path('collections/<int:collection_id>/notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('collections/<int:collection_id>/notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),

]