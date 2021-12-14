from django.contrib.auth.models import User
from . models import Genre, Language, Book, BookInstance, Author
from rest_framework import serializers


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title',
                  'author',
                  'isbn',
                  'genre',
                  'language',
                  ]
        extra_kwargs = {
            'summary': {'required': False},
        }


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'