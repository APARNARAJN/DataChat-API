from django.urls import path
from .views import QueryView, HistoryView, QueryDetailView

urlpatterns = [
    path('query/', QueryView.as_view(), name='query'),
    path('history/', HistoryView.as_view(), name='history'),
    path('history/<int:pk>/', QueryDetailView.as_view(), name='query-detail'),
]