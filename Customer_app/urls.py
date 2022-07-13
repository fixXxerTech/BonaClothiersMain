from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('',
         views.HomePageView.as_view(),
         name="HomePageView"),
    path('order/',
         views.OrderPageView.as_view(),
         name="OrderPageView"),
    path('pay/',
         views.PaymentPageView.as_view(),
         name="PaymentPageView"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
