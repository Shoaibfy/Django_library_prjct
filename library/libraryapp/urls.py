from django.urls import path,include
from .views import BookListAPIView,BookCreateAPIView,BookDestroyAPIView,BookUpadteList

urlpatterns=[
    path('book/',BookListAPIView.as_view(),name="booklist"),
    path('book/add/',BookCreateAPIView.as_view(),name="bookadd"),
     path('book/del/<int:pk>',BookDestroyAPIView.as_view(),name="bookdel"),
     path('book/upd/<int:pk>',BookUpadteList.as_view(),name="bookupdate"),



]