from rest_framework.serializers import ModelSerializer
from Boogging_app.models import BlogPost

class BlogpostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'