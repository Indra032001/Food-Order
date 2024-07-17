from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Add_View),
    path('show/', views.Show_View),
    path('update/<i>/', views.Update_view),
    path('delete/<i>/', views.Delete_view)
]
