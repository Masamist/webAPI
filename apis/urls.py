from django.urls import path
from .views import BookAPIView

# serializer

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),

]
