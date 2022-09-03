from rest_framework.viewsets import ModelViewSet
from core.models import Product
from core.serializers import ProductSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

