from django.urls import path
from Boogging_app.API.views import BlogListCreateAPIView

urlpatterns = [
    path('', BlogListCreateAPIView.as_view()),


]

