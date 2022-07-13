from django.db import models
from django.apps import apps
from datetime import date, datetime
from django.contrib.auth import get_user_model


# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# To get the model from the other app
# ------------------------------------
# outfit_model = apps.get_model("C_app", "InventoryModel")

# To get the current date and time to be used in the path
# --------------------------------------------------------
today = datetime.now()
# Month abbreviation, day and year  
todaysdate = today.strftime("%b-%dth-%Y-%H_hrs-%M_mins-%S_secs")

def InventoryPhotoRename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Outfits/<date&time>/<new_file_name>
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    return '{folder}/{date}/{name}.{extension}'.format(folder='Outfits', date=todaysdate, name=f"{instance.outfit_name}_{instance.pk}", extension=ext)

def ColorPhotoRename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Colors/<date&time>/<new_file_name>
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    return '{folder}/{date}/{name}.{extension}'.format(folder='Colors', date=todaysdate, name=instance.color_name, extension=ext)

def StylePhotoRename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Styles/<date&time>/<new_file_name>
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    return '{folder}/{date}/{name}.{extension}'.format(folder='Styles', date=todaysdate, name=f"{instance.style_name}_{instance.pk}", extension=ext)
  
# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<customid>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.userprofile.customid, filename)

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<customid>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.userprofile.customid, filename)

class InventoryModel(models.Model):
    active_manager = models.ForeignKey(
        Authenticated_manager,
        on_delete=models.CASCADE,
        verbose_name="auth_manager",
        related_name="manager_data",
        blank=True,
        null=True,
    )
    outfit_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    outfit_measurement_type = models.CharField(
        max_length=1500,
        blank=False,
        null=False,
    )
    outfit_price = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    record_date_edited = models.DateTimeField(
        auto_now=True,
    )
    record_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "{manager} added outfit: {name} on {date}".format(manager=self.active_manager.username, name=self.outfit_price, date=self.record_date)


class OutfitColorsModel(models.Model):
    active_manager = models.ForeignKey(
        Authenticated_manager,
        on_delete=models.CASCADE,
        verbose_name="auth_manager",
        related_name="manager_color_data",
        blank=True,
        null=True,
    )
    color_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    color_image = models.ImageField(
        null=False,
        blank=False,
        upload_to=ColorPhotoRename,
    )
    record_date_edited = models.DateTimeField(
        auto_now=True,
    )
    record_date = models.DateTimeField(
        auto_now_add=True,
    )
    def __str__(self):
        return "{manager} added color: {name} on {date}".format(manager=self.active_manager.username, name=self.color_name, date=self.record_date)


class OrderModel(models.Model):
    outfit_ordered = models.ForeignKey(
        InventoryModel,
        on_delete=models.CASCADE,
        verbose_name="outfit_info",
        related_name="ordered_outfit_data",
        blank=True,
        null=True,
    )
    material_quality = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    outfit_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    material_color = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    length = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    waist = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    laps = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    knees = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    ankles = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    style_image = models.ImageField(
        null=False,
        blank=False,
    )
    wrist_measurment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    lower_arm_measurment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    upper_arm_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    sleeve_length_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    tummy_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    chest_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    shoulder_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    neck_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    sleeve_type = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    button_type = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    order_remark = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    order_quantity = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    order_status = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    order_total_amount = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    customer_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_phone = models.CharField(
        help_text='Customer phone number',
        max_length=20,
        blank=False,
        null=False,
    )
    customer_email = models.EmailField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_state = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_address = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    deliver_date = models.DateTimeField(
        default=0,
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "{quantity}x {outfit} ordered on {date}".format(quantity=self.order_quantity, outfit=self.outfit_name, date=self.date_ordered)


class DeliverySettings(models.Model):
    active_manager = models.ForeignKey(
        Authenticated_manager,
        on_delete=models.CASCADE,
        verbose_name="auth_manager",
        related_name="delivery_manager",
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=1500,
        blank=False,
        null=False,
    )
    delivery_rate = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    # order_status = models.CharField(
    #     max_length=1000,
    #     null=False,
    #     blank=False,
    # )
    # customer_address = models.CharField(
    #     max_length=1000,
    #     null=False,
    #     blank=False,
    # )
    record_date_edited = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    record_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )

    def __str__(self):
        return "{state} state delivery rate: {delivery_rate} by: {manager} added on {date}".format(state=self.state, delivery_rate=self.delivery_rate, manager=self.active_manager, date=self.record_date)


class OutfitImageModel(models.Model):
    outfit_ordered = models.ForeignKey(
        InventoryModel,
        on_delete=models.CASCADE,
        verbose_name="outfit_info",
        related_name="outfit_data",
        blank=True,
        null=True,
    )
    outfit_image = models.ImageField()


class TransporterModel(models.Model):
    transporter_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    record_date_edited = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    record_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )

    def __str__(self):
        return "Transporter: {transport_name} added on {date}".format(transport_name=self.transporter_name, date=self.record_date)


class StyleImageModel(models.Model):
    style_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    style_image = models.ImageField(
        null=False,
        blank=False,
        upload_to=StylePhotoRename,
    )
    record_date_edited = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    record_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )

    def __str__(self):
        return "Style name: {style_name} added on {date}".format(state=self.style_name, date=self.record_date)
