from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup-provider/', views.signup_provider, name='signup_provider'),
    path('signup-consumer/', views.signup_consumer, name='signup_consumer'), 
    path('login/', views.login_view, name='login'), 
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('mentor/<int:id>/', views.mentor_detail, name='mentor_detail'),

]
