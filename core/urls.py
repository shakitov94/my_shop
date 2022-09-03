from django.urls import path
from core.views import ProductView


urlpatterns = [
    path('', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', ProductView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),

]
