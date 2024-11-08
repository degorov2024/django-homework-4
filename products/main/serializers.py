from rest_framework import serializers

from main.models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)

    #Альтернативно, можно было не указывать параметр source, а вместо этого
    #обозвать переменную ниже как comments (это related_name во внешнем ключе)
    reviews = ReviewSerializer(many=True, read_only=True, source='comments')
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']