from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_ser=serializers.CharField(source='author_name.author_name')
    category_ser=serializers.CharField(source='category_name.category_name')
    class Meta:
        model=Book
        fields=('book_name','book_price','book_isbn_Num','author_ser','category_ser',)


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=('pk','book_name','book_price','book_isbn_Num','author_name','category_name',)