from django.urls import path
from . import views


urlpatterns = [
     path('',views.LandingPage,name='landing'),
    path('signup/', views.signupPage, name='signup'),
    path('home/', views.Home, name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('predict', views.Predict, name='predict'),
    path('result',views.Result,name='result'),
    path('about_us/', views.about_us, name='about_us'),
    
]


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),

     path('result',views.Result,name='result'),
     path('team',views.About,name='team'),
     path('predict', views.Predict, name='predict'),
    
]
'''



