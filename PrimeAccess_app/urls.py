from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('',
         views.PrimeAccessView.as_view(),
         name="PrimeAccessView"),

    path('all-colors/',
         views.AllColorsView.as_view(),
         name="AllColorsView"),
    path('all-colors/<action>/<instance>/',
         views.ModifyColorsView.as_view(),
         name="ModifyColorsView"),

    path('all-styles/',
         views.AllStylesView.as_view(),
         name="AllStylesView"),
    path('all-styles/<action>/<instance>/',
         views.ModifyStylesView.as_view(),
         name="ModifyStylesView"),

    path('all-products/',
         views.AllProductsView.as_view(),
         name="AllProductsView"),
    path('all-products/<action>/<instance>/',
         views.ModifyProductsView.as_view(),
         name="ModifyProductsView"),

    path('all-orders/',
         views.AllOrdersView.as_view(),
         name="AllOrdersView"),
    path('all-orders/',
         views.AllOrdersView.as_view(),
         name="AllOrdersView"),

    path('delivery-settings/',
         views.DeliverySettings.as_view(),
         name="DeliverySettingsView"),
    path('delivery-settings/<action>/<instance>/',
         views.ModifyDeliverySettings.as_view(),
         name="DeliverySettingsModificationView"),

    path('add-transporter/',
         views.AddTransporterView.as_view(),
         name="AddTransporterView"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)