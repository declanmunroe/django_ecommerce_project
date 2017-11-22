from django.conf.urls import url
from .views import all_products


urlpatterns = [
    url(r"^all_products", all_products, name = "all_products"),
    ]