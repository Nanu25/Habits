from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_habit", views.add_habit, name="add_habit"),
    path('main', views.main_page, name='main_page'),
    path('mark_done/<int:habit_id>/', views.mark_done, name='mark_done'),
    path('top_habits', views.top_habits, name='top_habits'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)