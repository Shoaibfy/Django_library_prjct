from .models import Book
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .serializer import BookSerializer,BookCreateSerializer


class BookListAPIView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer

class BookCreateAPIView(CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer


class BookDestroyAPIView(DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer
    lookup_field='pk'


class BookUpadteList(UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer
    lookup_field='pk'
