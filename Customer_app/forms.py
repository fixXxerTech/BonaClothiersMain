from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# To get the model from the other app
# ------------------------------------
OrderModel = apps.get_model("PrimeAccess_app", "OrderModel")


class OrderForm(forms.ModelForm):

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
    # )

    class Meta:
        model = OrderModel
        fields = (
            'order_status',
            'order_remark',
            'order_quantity',
            'customer_address',
        )

        exclude = (
            'deliver_date',
            'date_ordered',
            'product_ordered',
        )

    def save(self, commit=True):
        OrderModel = super(OrderForm, self).save(commit=False)
        OrderModel.order_status = self.cleaned_data['order_status']
        OrderModel.order_remark = self.cleaned_data['order_remark']
        OrderModel.order_quantity = self.cleaned_data['order_quantity']
        OrderModel.product_ordered = self.cleaned_data['product_ordered']

        if commit:
            OrderModel.save()

        return OrderModel
