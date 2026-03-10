from django.urls import path
from . import views

# เช็คตัวสะกดตรงนี้ครับ ต้องเป็น urlpatterns (มี s และเป็น list [])
urlpatterns = [
    path('members/', views.members, name='members'),
]