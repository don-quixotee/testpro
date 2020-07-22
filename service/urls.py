from django.urls import path
from .views import index, detailview

urlpatterns = [
    path('', index , name='home'),
    path('detail/', detailview, name='detail'),
]