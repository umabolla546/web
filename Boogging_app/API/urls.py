from django.urls import path
from Boogging_app.API.views import BloagListCreateAPIView

urlpatterns = [
    path('', BloagListCreateAPIView.as_view()),


]

