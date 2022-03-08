from django.contrib import admin
from django.urls import path
from .views import HomeView, AboutView, ExploreView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home.html"),
    path('about/', AboutView.as_view(), name="about.html"),
    path('explore/', ExploreView.as_view(), name="explore.html"),
    path('contact/', ContactView.as_view(), name="contact.html"),

]
