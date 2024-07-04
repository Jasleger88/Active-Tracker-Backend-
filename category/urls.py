from django.urls import path
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>/', CategoryListView.as_view()),
]