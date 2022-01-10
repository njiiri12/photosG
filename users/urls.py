from django.urls import path
from users import views

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

]