from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user_profile/', views.user_profile_view, name='user_profile'),
    #path('pilot_list/', views.PilotsListView.as_view(), name='pilots_list')
    path('pilot_list/', views.pilot_list_view, name='pilots_list')
]
