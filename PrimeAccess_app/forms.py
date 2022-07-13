from . import models
from django import forms
from django.apps import apps
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# To get the model from the other app
# ------------------------------------


# A drop down list of all Nigerian States
# ----------------------------------------
NIGERIAN_STATES = (

    ("", "----------"),
    ("Abuja FCT", "Abuja FCT"),
    ("Abia", "Abia"),
    ("Adamawa", "Adamawa"),
    ("Akwa Ibom", "Akwa Ibom"),
    ("Anambara", "Anambara"),
    ("Bauchi", "Bauchi"),
    ("Bayelsa", "Bayelsa"),
    ("Benue", "Benue"),
    ("Borno", "Borno"),
    ("Cross River", "Cross River"),
    ("Delta", "Delta"),
    ("Ebonyi", "Ebonyi"),
    ("Edo", "Edo"),
    ("Ekiti", "Ekiti"),
    ("Enugu", "Enugu"),
    ("Gombe", "Gombe"),
    ("Imo", "Imo"),
    ("Jigawa", "Jigawa"),
    ("Kaduna", "Kaduna"),
    ("Kano", "Kano"),
    ("Katsina", "Katsina"),
    ("Kebbi", "Kebbi"),
    ("Kogi", "Kogi"),
    ("Kwara", "Kwara"),
    ("Lagos", "Lagos"),
    ("Nassarawa", "Nassarawa"),
    ("Niger", "Niger"),
    ("Ogun", "Ogun"),
    ("Ondo", "Ondo"),
    ("Osun", "Osun"),
    ("Oyo", "Oyo"),
    ("Plateau", "Plateau"),
    ("Rivers", "Rivers"),
    ("Sokoto", "Sokoto"),
    ("Taraba", "Taraba"),
    ("Yobe", "Yobe"),
    ("Zamfara", "Zamfara"),
    ("Outside Nigeria", "Outside Nigeria"),
)

# A drop down list of all Outfit Measure Type States
# ---------------------------------------------------
OUTFIT_MEASUREMENT_TYPES = (

    ("", "----------"),
    ("Long Sleeve", "Long Sleeve"),
    ("3/4 Sleeve", "3/4 Sleeve"),
    ("Short Sleev", "Short Sleeve"),
    ("Trouser", "Trouser"),
    ("Short", "Short"),
    ("Agbada Sleeve", "Agbada Sleeve"),
)

# A drop down list of all Outfit Names 
# -------------------------------------
OUTFIT_NAMES = (

    ("", "----------"),
    ("Senator", "Senator"),
    ("Ankara", "Ankara"),
    ("Beach wear", "Beach wear"),
    ("Ishiagu", "Ishiagu"),
    ("Agbada", "Agbada"),
)

# <select name="state" id="state">
#               <option value="" selected="selected">- Select -</option>
#               <option value="Abuja FCT">Abuja FCT</option>
#               <option value="Abia">Abia</option>
#               <option value="Adamawa">Adamawa</option>
#               <option value="Akwa Ibom">Akwa Ibom</option>
#               <option value="Anambra">Anambra</option>
#               <option value="Bauchi">Bauchi</option>
#               <option value="Bayelsa">Bayelsa</option>
#               <option value="Benue">Benue</option>
#               <option value="Borno">Borno</option>
#               <option value="Cross River">Cross River</option>
#               <option value="Delta">Delta</option>
#               <option value="Ebonyi">Ebonyi</option>
#               <option value="Edo">Edo</option>
#               <option value="Ekiti">Ekiti</option>
#               <option value="Enugu">Enugu</option>
#               <option value="Gombe">Gombe</option>
#               <option value="Imo">Imo</option>
#               <option value="Jigawa">Jigawa</option>
#               <option value="Kaduna">Kaduna</option>
#               <option value="Kano">Kano</option>
#               <option value="Katsina">Katsina</option>
#               <option value="Kebbi">Kebbi</option>
#               <option value="Kogi">Kogi</option>
#               <option value="Kwara">Kwara</option>
#               <option value="Lagos">Lagos</option>
#               <option value="Nassarawa">Nassarawa</option>
#               <option value="Niger">Niger</option>
#               <option value="Ogun">Ogun</option>
#               <option value="Ondo">Ondo</option>
#               <option value="Osun">Osun</option>
#               <option value="Oyo">Oyo</option>
#               <option value="Plateau">Plateau</option>
#               <option value="Rivers">Rivers</option>
#               <option value="Sokoto">Sokoto</option>
#               <option value="Taraba">Taraba</option>
#               <option value="Yobe">Yobe</option>
#               <option value="Zamfara">Zamfara</option>
#      <option value="Outside Nigeria">Outside Nigeria</option>
#             </select>

class InventoryForm(forms.ModelForm):

    outfit_name = forms.ChoiceField(
        label='Outfit Name',
        choices=OUTFIT_NAMES,
        widget=forms.Select(
            attrs={

                'name': 'outfit_name',
                'aria-label': 'outfit_name',
                'id': 'OutfitName',
                'class': 'form-select',

            }
        )
    )
    outfit_measurement_type = forms.ChoiceField(
        label='Measurement Type',
        choices=OUTFIT_MEASUREMENT_TYPES,
        widget=forms.Select(
            attrs={

                'name': 'outfit_measurement_type',
                'aria-label': 'outfit_measurement_type',
                'id': 'OutfitMeasurementType',
                'class': 'form-select',

            }
        )
    )
    # username = forms.CharField(
    #     label='User Name',
    #     widget=forms.TextInput(
    #         attrs={

    #             'type': 'text',
    #             'id': 'username',
    #             'name': 'username',
    #             'placeholder': '',
    #             'class': 'input--dark input--squared',
    #         }
    #     )
    # )

    # email = forms.CharField(
    #     label='Email Address',
    #     widget=forms.EmailInput(
    #         attrs={

    #             'type': 'email',
    #             'id': 'email',
    #             'name': 'email',
    #             'placeholder': '',
    #             'class': 'input--dark input--squared',

    #         }
    #     )
    # )

    # password1 = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(
    #         attrs={

    #             'type': 'password',
    #             'name': 'password1',
    #             'class': 'input--dark input--squared input--dark',

    #         }
    #     )
    # )

    # password2 = forms.CharField(
    #     label='Confirm Password',
    #     widget=forms.PasswordInput(
    #         attrs={

    #             'type': 'password',
    #             'name': 'password2',
    #             'class': 'input--dark input--squared',

    #         }
    #     )
    # )InventoryPhotoRename

    class Meta:
        model = models.InventoryModel
        fields = (
            'outfit_name',
            'outfit_price',
            'outfit_measurement_type',
        )

        exclude = (
            'record_date',
            'active_manager',
            'record_date_edited',
        )

    def save(self, commit=True):
        InventoryModelInstance = super(InventoryForm, self).save(commit=False)
        InventoryModelInstance.outfit_name = self.cleaned_data['outfit_name']
        InventoryModelInstance.outfit_price = self.cleaned_data['outfit_price']
        InventoryModelInstance.outfit_measurement_type = self.cleaned_data['outfit_measurement_type']

        if commit:
            InventoryModelInstance.save()

        return InventoryModelInstance


class DeliverySettngsForm(forms.ModelForm):
    state = forms.ChoiceField(
        label='State',
        choices=NIGERIAN_STATES,
        widget=forms.Select(
            attrs={

                'name': 'state',
                'aria-label': 'State',
                'id': 'floatingSelect',
                'class': 'form-select',

            }
        )
    )
    delivery_rate = forms.CharField(
        label='Rate',
        widget=forms.NumberInput(
            attrs={

                'type': 'number',
                'id': 'floatingZip',
                'maxlength': '10',
                'name': 'delivery-rate',
                'placeholder': '',
                'class': 'form-control',

            }
        )
    )

    class Meta:
        model = models.DeliverySettings
        fields = (
            'state',
            'delivery_rate',
        )
        exclude = (
            'rate_date',
            'rate_date_edited'
        )

    def save(self, commit=True):
        DeliverySettingsInstance = super(
            DeliverySettngsForm, self).save(commit=False)
        DeliverySettingsInstance.state = self.cleaned_data['state']
        DeliverySettingsInstance.delivery_rate = self.cleaned_data['delivery_rate']

        if commit:
            DeliverySettingsInstance.save()

        return DeliverySettingsInstance


class OrderForm(forms.ModelForm):
    outfit_name = forms.ModelChoiceField(
        queryset=models.InventoryModel.objects.all(),
        label='Outfit Name',
        empty_label="----------",
        widget=forms.Select(
            attrs={

                'type': 'select',
                'id': 'OutfitName',
                'name': 'outfit_name',
                'placeholder': '',
                'class': 'form-control',

            }
        )
    )

    class Meta:
        model = models.OrderModel
        exclude = (
            'deliver_date',
            'date_ordered',
            'outfit_ordered',
        )


class ColorForm(forms.ModelForm):
    class Meta:
        model = models.OutfitColorsModel
        exclude = (
            'deliver_date',
            'date_ordered',
            'active_manager',
        )


class TransporterForm(forms.ModelForm):
    class Meta:
        model = models.TransporterModel
        exclude = (
            'record_date',
            'active_manager',
            'record_date_edited',
        )


class StylesForm(forms.ModelForm):
    class Meta:
        model = models.StyleImageModel
        exclude = (
            'record_date',
            # 'active_manager',
            'record_date_edited',
        )



# class ColorForm(forms.ModelForm):
#     # color_name = forms.ModelChoiceField(
#     #     queryset=models.InventoryModel.objects.all(),
#     #     label='Outfit Name',
#     #     empty_label="----------",
#     #     widget=forms.Select(
#     #         attrs={

#     #             'type': 'select',
#     #             'id': 'outfit-name',
#     #             'name': 'outfit-name',
#     #             'placeholder': '',
#     #             'class': 'form-control',

#     #         }
#     #     )
#     # )

#     class Meta:
#         model = models.OutfitColorsModel
#         exclude = (
#             'deliver_date',
#             'date_ordered',
#             'active_manager',
#         )