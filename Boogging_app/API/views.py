from rest_framework import generics
from Boogging_app.models import BlogPost
from .serializers import BlogpostSerializer



class BloagListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer