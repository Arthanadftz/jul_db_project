from django.urls import path

from . import views

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournament_list'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('new/', views.TournamentCreateView.as_view(), name='tournament_new'),
    #path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    #path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
