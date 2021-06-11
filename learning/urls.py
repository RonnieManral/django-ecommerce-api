from django.urls import path, include
from .views import ListCategory,ListBook,ListProduct,DetailCategory,DetailProduct,DetailBook
urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategories'),

    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name='singlebook'),
    
    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='singleproducts')
]
