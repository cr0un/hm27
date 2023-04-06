from django.urls import path
from . import views
from django.contrib import admin
from .views import AdView, AdDetailView, CategoriesView, CategoryDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', CategoriesView.as_view(), name='categories_list'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('ad/', AdView.as_view(), name='ads_list'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('admin/', admin.site.urls),
]
