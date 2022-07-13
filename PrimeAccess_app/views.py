from . import forms
from . import models

from pprint import pprint
from django.apps import apps
from django.utils import timezone
from django.contrib import messages
from os.path import join as join_path
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic.base import View as custom_view
from django.contrib.auth.mixins import LoginRequiredMixin


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


class PrimeAccessView(LoginRequiredMixin, custom_view):
    template_name = join_path("dashboard", "prime-access.html")

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


class AllColorsView(LoginRequiredMixin, custom_view):
    template_name = join_path("dashboard", "all-colors.html")

    def get(self, request):
        all_colors = reversed(models.OutfitColorsModel.objects.all())
        form_class = forms.ColorForm()

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_colors": all_colors,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        all_colors = reversed(models.OutfitColorsModel.objects.all())
        form_class = forms.ColorForm(request.POST, request.FILES)

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_colors": all_colors,
        }

        if form_class.is_valid():
            form_instance = form_class.save(commit=False)
            form_instance.active_manager = request.user
            form_instance.save()
            messages.success(request, "New Color Added Successfully")
            return redirect(reverse("AllColorsView"))
        else:
            print(form_class.errors)

        return render(request, self.template_name, context=context)


class ModifyColorsView(LoginRequiredMixin, custom_view):
    action = "update"
    template_name = join_path("dashboard", "all-colors.html")
    edit_template_name = join_path("dashboard", "edit-colors.html")

    def get(self, request, action, instance):

        if action == "delete":
            models.OutfitColorsModel.objects.get(pk=instance).delete()
            return redirect(reverse("AllColorsView"))
        elif action == "update":
            all_colors = reversed(models.OutfitColorsModel.objects.all())
            color_record = models.OutfitColorsModel.objects.get(
                pk=instance)
            form_class = forms.ColorForm(instance=color_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_colors": all_colors,
            }
            return render(request, self.edit_template_name, context=context)

        return render(request, self.template_name, context=context)

    def post(self, request, action, instance):
        if action == "update":
            all_colors = reversed(models.OutfitColorsModel.objects.all())
            color_record = models.OutfitColorsModel.objects.get(
                pk=instance)
            form_class = forms.ColorForm(
                data=request.POST, files=request.FILES, instance=color_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_colors": all_colors,
            }

            if form_class.is_valid():
                form_class.save()
                messages.success(request, "Color Updated Successfully")
                return redirect(reverse("AllColorsView"))

        return render(request, self.template_name, context=context)


class AllStylesView(LoginRequiredMixin, custom_view):
    template_name = join_path("dashboard", "all-styles.html")

    def get(self, request):
        all_styles = reversed(models.StyleImageModel.objects.all())
        form_class = forms.StylesForm()

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_styles": all_styles,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        all_styles = reversed(models.StyleImageModel.objects.all())
        form_class = forms.StylesForm(request.POST, request.FILES)

        context = {
            "form": form_class,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_styles": all_styles,
        }

        if form_class.is_valid():
            form_class.save()
            messages.success(request, "New Style Added Successfully")
            return redirect(reverse("AllStylesView"))
        else:
            print(form_class.errors)

        return render(request, self.template_name, context=context)


class ModifyStylesView(LoginRequiredMixin, custom_view):
    action = "update"
    template_name = join_path("dashboard", "all-styles.html")
    edit_template_name = join_path("dashboard", "edit-styles.html")

    def get(self, request, action, instance):
        if action == "delete":
            models.StyleImageModel.objects.get(pk=instance).delete()
            return redirect(reverse("AllStylesView"))
        elif action == "update":
            all_styles = reversed(models.StyleImageModel.objects.all())
            style_record = models.StyleImageModel.objects.get(
                pk=instance)
            form_class = forms.StylesForm(instance=style_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_colors": all_styles,
            }
            return render(request, self.edit_template_name, context=context)

        return render(request, self.template_name, context=context)

    def post(self, request, action, instance):
        if action == "update":
            all_styles = reversed(models.StyleImageModel.objects.all())
            style_record = models.StyleImageModel.objects.get(
                pk=instance)
            form_class = forms.StylesForm(
                data=request.POST, files=request.FILES, instance=style_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_colors": all_styles,
            }

            if form_class.is_valid():
                form_class.save()
                messages.success(request, "Style Updated Successfully")
                return redirect(reverse("AllStylesView"))

        return render(request, self.template_name, context=context)


class AllProductsView(LoginRequiredMixin, custom_view):
    action = "create"
    template_name = join_path("dashboard", "all-outfits.html")

    def get(self, request):
        form_class = forms.InventoryForm()
        outfit_inventory = reversed(models.InventoryModel.objects.all())

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_inventory": outfit_inventory,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form_class = forms.InventoryForm(request.POST, request.FILES)
        outfit_inventory = reversed(models.InventoryModel.objects.all())

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "outfit_inventory": outfit_inventory,
        }

        if form_class.is_valid():
            form_instance = form_class.save(commit=False)
            form_instance.active_manager = request.user
            form_instance.save()
            messages.success(request, "New Outfit Added Successfully")
            return redirect(reverse("AllProductsView"))

        return render(request, self.template_name, context=context)


class ModifyProductsView(LoginRequiredMixin, custom_view):
    action = "update"
    template_name = join_path("dashboard", "all-outfits.html")
    edit_template_name = join_path("dashboard", "edit-outfit.html")

    def get(self, request, action, instance):
        if action == "delete":
            models.InventoryModel.objects.get(pk=instance).delete()
            messages.success(request, "Outfit Deleted Successfully")
            return redirect(reverse("AllProductsView"))
        elif action == "update":
            outfit_inventory = reversed(models.InventoryModel.objects.all())
            outfit_record = models.InventoryModel.objects.get(
                pk=instance)
            form_class = forms.InventoryForm(instance=outfit_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_inventory": outfit_inventory,
            }
            # return render(request, self.edit_template_name, context=context)

        return render(request, self.template_name, context=context)

    def post(self, request, action, instance):
        if action == "update":
            outfit_inventory = reversed(models.InventoryModel.objects.all())
            outfit_record = models.InventoryModel.objects.get(
                pk=instance)
            form_class = forms.InventoryForm(
                data=request.POST, files=request.FILES, instance=outfit_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "outfit_inventory": outfit_inventory,
            }

            if form_class.is_valid():
                form_class.save()
                messages.success(request, "Outfit Updated Successfully")
                return redirect(reverse("AllProductsView"))

        return render(request, self.template_name, context=context)


class AllOrdersView(LoginRequiredMixin, custom_view):
    template_name = join_path("dashboard", "all-orders.html")

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


class DeliverySettings(LoginRequiredMixin, custom_view):
    action = "create"
    template_name = join_path("dashboard", "delivery-settings.html")

    def get(self, request):
        form_class = forms.DeliverySettngsForm()
        transporter_form = forms.TransporterForm()
        delivery_record = models.DeliverySettings.objects.all()
        try:
            transporter_instance = models.TransporterModel.objects.all().latest("id")
        except:
            transporter_instance = models.TransporterModel.objects.all()

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "transporter_form": transporter_form,
            "delivery_record": reversed(delivery_record),
            "transporter_instance": transporter_instance,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form_class = forms.DeliverySettngsForm(request.POST)
        delivery_record = models.DeliverySettings.objects.all()
        try:
            transporter_instance = models.TransporterModel.objects.all().latest("id")
        except:
            transporter_instance = models.TransporterModel.objects.all()

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "delivery_record": reversed(delivery_record),
            "transporter_instance": transporter_instance,
        }

        if form_class.is_valid():
            form_class.save(commit=False)
            form_class.active_manager = request.user
            form_class.save()
            return redirect(reverse('DeliverySettingsView'))

        return render(request, self.template_name, context=context)


class ModifyDeliverySettings(LoginRequiredMixin, custom_view):
    action = "update"
    template_name = join_path("dashboard", "delivery-settings.html")

    def get(self, request, action, instance):

        if action == "delete":
            models.DeliverySettings.objects.get(pk=instance).delete()
            return redirect(reverse("DeliverySettingsView"))
        elif action == "update":
            all_delivery_record = models.DeliverySettings.objects.all()
            delivery_record = models.DeliverySettings.objects.get(
                pk=instance)
            form_class = forms.DeliverySettngsForm(instance=delivery_record)

            try:
                transporter_instance = models.TransporterModel.objects.all().latest("id")
            except:
                transporter_instance = models.TransporterModel.objects.all()

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "delivery_record": all_delivery_record,
                "transporter_instance": transporter_instance,
                # "delivery_record": reversed(instance_date),
            }

        return render(request, self.template_name, context=context)

    def post(self, request, action, instance):
        if action == "update":
            all_delivery_record = models.DeliverySettings.objects.all()
            delivery_record = models.DeliverySettings.objects.get(
                pk=instance)
            form_class = forms.DeliverySettngsForm(
                data=request.POST, instance=delivery_record)

            try:
                transporter_instance = models.TransporterModel.objects.all().latest("id")
            except:
                transporter_instance = models.TransporterModel.objects.all()

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "delivery_record": all_delivery_record,
                "transporter_instance": transporter_instance,
                # "delivery_record": reversed(instance_date),
            }

            if form_class.is_valid():
                form_class.save()
                return redirect(reverse("DeliverySettingsView"))

        return render(request, self.template_name, context=context)


class AddTransporterView(LoginRequiredMixin, custom_view):

    def post(self, request):
        try:
            transporter_instance = models.TransporterModel.objects.all().latest("id")
            transporter_form = forms.TransporterForm(
                data=request.POST, instance=transporter_instance)
        except:
            transporter_form = forms.TransporterForm(data=request.POST)

        if transporter_form.is_valid():
            transporter_form.save()
            return redirect(reverse('DeliverySettingsView'))
        else:
            print(transporter_form.errors)
            return redirect(reverse('DeliverySettingsView'))
