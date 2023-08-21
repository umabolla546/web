from rest_framework import generics
from Boogging_app.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

import logging

logger = logging.getLogger('info_logger')


from rest_framework import status
from rest_framework.response import Response

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            logger.error("Validation error creating blog post: %s", str(e))
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Error creating blog post: %s", str(e))
            return Response({"error": "An error occurred while creating the blog post..."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

