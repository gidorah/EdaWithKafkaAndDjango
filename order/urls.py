from django.urls import path

from order import views

app_name = "order"
urlpatterns = [path("", views.order_list, name="order_list")]
