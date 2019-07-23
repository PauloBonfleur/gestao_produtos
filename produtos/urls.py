from django.urls import path
from .views import prod_update
from .views import prod_new
from .views import prod_list
from .views import prod_delete

urlpatterns = [
    path('list/', prod_list, name='prod_list'),
    path('new/', prod_new, name='prod_new'),
    path('update/<int:id>/', prod_update, name='prod_update'),
    path('delete/<int:id>/', prod_delete, name='prod_delete')
]
