from category import Category
from rest_framework import serializers

from applications.product.models import Product, Image, Rating, Categore


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categore
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Rating
        fields = 'rating', 'owner'


class ProductImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ProductImagesSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'owner', 'name', 'description', 'price', 'category', 'images', 'rating')

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(**validated_data)
        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rating_result = 0
        for i in instance.rating.all():
            rating_result += int(i.rating)
        if instance.rating.all().count() == 0:
            representation['rating'] = rating_result
        else:
            representation['rating'] = rating_result / instance.rating.all().count()
        return representation