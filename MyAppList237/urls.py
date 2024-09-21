from django.urls import path
from MyAppList237.views import index, update, delete

urlpatterns = [
  path('', index, name='index'),
  path('<int:my_id>/update', update, name='update'),
  path('<int:my_id>/delete', delete, name='delete')
]