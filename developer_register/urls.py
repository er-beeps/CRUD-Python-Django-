from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.developer_form,name='developer_insert'),
    path('<int:id>/', views.developer_form,name='developer_update'),
    path('delete/<int:id>/', views.developer_delete,name='developer_delete'),
    path('list/', views.developer_list,name='developer_list')
]
   