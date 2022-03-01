from django.contrib import admin
from django.urls import path
from .views import homepage, aboutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('about/', aboutpage, name="aboutpage"),

]
