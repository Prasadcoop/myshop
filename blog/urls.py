
from django.urls import path
from.import views
urlpatterns = [
    path("", views.support, name="index"),

    path("about/", views.about, name="About us"),
    path("contact/", views.phone1, name="contact us"),
    path("tracker/", views.tracker, name="trackingstatus"),
    path("search", views.search, name="search"),
    path("product/<int:myid>", views.productView, name="product view"),
    path("checkout/", views.checkout, name="checkout"),
    path("support/", views.support, name="support"),
    path("footer/", views.footer, name="footer"),

]