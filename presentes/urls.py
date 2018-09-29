from django.urls import path
from .views import PresenteList, PresenteCreate, PresenteUpdate, PresenteDelete

urlpatterns = [
    path('', PresenteList.as_view(), name='presente_list'),
    path('create/', PresenteCreate.as_view(), name='presente_create'),
    path('update/<int:pk>/', PresenteUpdate.as_view(), name='presente_update'),
    path('delete/<int:pk>', PresenteDelete.as_view(), name='presente_delete'),
]
