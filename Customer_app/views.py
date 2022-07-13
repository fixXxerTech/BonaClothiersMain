from . import forms

from pprint import pprint
# from django.apps import apps
from django.utils import timezone
from os.path import join as join_path
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from django.views.generic.base import View as custom_view
from Auth_app.helpers import EmailManager

# GET Current date and time.
# ---------------------------
Todays_Date = timezone.now()
Todays_Date = Todays_Date.strftime("%Y")

# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# SET admin acess title.
# -----------------------
panel_name = "Prime Access"


class HomePageView(custom_view):
    template_name = join_path("Customer_templates", "home.html")

    def get(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class OrderPageView(custom_view):
    template_name = join_path("Customer_templates", "order.html")

    def get(self, request):
        form_class = forms.OrderForm()

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form_class = forms.OrderForm(request.POST, request.FILES)

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class PaymentPageView(custom_view):
    template_name = join_path("Customer_templates", "payment.html")

    def get(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)
