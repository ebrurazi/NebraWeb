from django.contrib import admin
from django.urls import path
from core import views as core_views
from library import views as library_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",core_views.home, name = "home"),

    path('add-book', library_views.add_book, name='add_book'),
    path('book/<int:pk>/', library_views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', library_views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', library_views.delete_book, name='delete_book'),

    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',core_views.signup, name='signup'),
]
