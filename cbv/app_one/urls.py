from django.urls import path
from app_one import views

app_name = 'app_one'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
]