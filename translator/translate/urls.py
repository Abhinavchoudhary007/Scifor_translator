from django.urls import path
from .views import home_view, translate_view, delete_translation

urlpatterns = [
    path('', home_view, name='home'),
    path('translate/', translate_view, name='translate'),
    path('delete/<int:translation_id>/', delete_translation, name='delete_translation'),
]