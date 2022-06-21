from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('napisz', views.napisz, name='napisz'),
    path('sposoby', views.sposoby, name='sposoby'),
    path('logout', views.logout, name='logout'),
    path('napisz_create', views.napiszCreate, name='napiszCreate'),
    path('napisz_update/<str:pk>/', views.napiszUpdate, name='napiszUpdate'),
    path('napisz_delete/<str:pk>/', views.napiszDelete, name='napiszDelete'),
]