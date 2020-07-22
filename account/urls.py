from django.urls import path , include
from .views import SignUpView


urlpatterns = [
    
    path('', include('django.contrib.auth.urls')),
    path('signUp/', SignUpView.as_view(), name='signUp')
]