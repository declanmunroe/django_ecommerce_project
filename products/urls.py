from django.conf.urls import url
from .views import all_products, do_search


urlpatterns = [
    url(r"^all_products", all_products, name = "all_products"),
    url(r"^search", do_search, name = "search"),
    ]