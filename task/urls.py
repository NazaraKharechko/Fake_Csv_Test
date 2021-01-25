from django.urls import path
from . import views
from .views import all_shem, save_schemas, CreateVieAll
urlpatterns = [
    path('', views.user_login, name='login'),
    path('all/', views.all_shem),
    path('save/', views.save_schemas),
    path('alls/<int:pk>', CreateVieAll.as_view()),
]
