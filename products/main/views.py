from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review

@api_view(['GET'])
def products_list_view(request):
    """Получение всех товаров из БД"""
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """Получение товара по id (если его нет, то 404)"""
        the_product = get_object_or_404(Product, id=product_id)
        ser = ProductDetailsSerializer(instance=the_product, many=False)
        return Response(ser.data)

# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass