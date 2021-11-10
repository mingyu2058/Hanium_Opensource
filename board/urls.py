from django.urls import path
from . import views

urlpatterns = [
    path('board', views.index,name='board'),
    path('write', views.post,name='write'),
    path('write/<int:id>',views.detail,name='detail'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]
