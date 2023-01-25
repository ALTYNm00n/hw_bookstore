from rest_framework import serializers,exceptions

from mayapp.models import (
    BookCategory,Book,Author
)

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = (
            'name', 'image', 'id'
        )

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =(
            'book_amount',  'date_birthday', 'pseudonym', 'avatar' ,

        )
        read_only_fields = (
            'book_category',
        )

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =(
            'name', 'date_of_issue', 'price',  
            'chapter_amount', 'prewiew', 
        )
        read_only_fields = (
            'book_category','author',
        )

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()


    def validate_password (self, value):
        if len(value) < 8:
            raise exceptions.ValidationError('Password is too short ')
        elif len(value) >  24:
            raise exceptions.ValidationError("Password is too long")
        return value


class AuthorizarionSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

