from audioop import reverse
from pydoc import resolve

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from django.urls import reverse
from nocportal.models import NocComment



# Create your models here.
DELIVERY_TYPE = (
    ("Single MPLS", "Single MPLS"),
    ("Single Internet", "Single Internet"),
    ("MPLS + Internet", "MPLS + Internet"),
    ("Double MPLS", "Double MPLS"),
    ("Double Internet", "Double Internet"),
)

PARRAREL =  (
    (1, 'Parallel move'),
    (2, 'Hot-cut ')
)

DIVISION = (
    (1, 'Road'),
    (2, 'Air & Sea'),
    (3, 'Solutions'),
)

CLASSIFICATION = (
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
    ('Bronze', 'Bronze'),
)

BOLEAN = (
    (True, 'Yes'),
    (False, 'No')
)

OFFICE_HOURS = (
    (1, '7-17'),
    (2, '8-16'),
    (3, '24/7')
)

class SiteVendor(models.Model):
    site_code = models.CharField(verbose_name="Site Code", max_length=10, help_text='Code requested by Vendor Team')
    delivery_type = models.CharField(choices=DELIVERY_TYPE, verbose_name='Type of delivery', max_length=64)
    address = models.CharField(verbose_name="Site Address", max_length=64)
    bandwidth = models.IntegerField(verbose_name="Bandwidth")
    # Site Classification
    site_classification = models.CharField(choices=CLASSIFICATION, verbose_name="Site Classification:", max_length=64)
    # Other Information
    # instalation_date = models.CharField(verbose_name="Date when line will be installed on site?", max_length=64)
    # local_contact = models.CharField(verbose_name="???Contact to person on site???", max_length=64)
    # technical_contact = models.CharField(verbose_name="???Contact to person on site???", max_length=64)
    # lan_assistance = models.BooleanField(choices=BOLEAN, verbose_name="Do you need assistance with LAN?")
    # voip_assistance = models.BooleanField(choices=BOLEAN, verbose_name="Do you need VoIP on site?")
    # parrarelorhot = models.IntegerField(verbose_name="Parallel move or hot-cut ?", choices=PARRAREL)
    # Site Detail
    # company_name = models.CharField(verbose_name="Company Name:", max_length=64)
    # city = models.CharField(verbose_name="City:", max_length=64)
    # address_2 = models.CharField(verbose_name="Address:", max_length=64)
    # post_code = models.CharField(verbose_name="Postal Code:", max_length=64)
    # country = models.CharField(verbose_name="Country:", max_length=64)
    # office_hours = models.IntegerField(choices=OFFICE_HOURS, verbose_name="Office Hours:")
    # division = models.IntegerField(choices=DIVISION ,verbose_name="Division:")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # AttachFIle
    # file = models.FileField(null=True, blank=True, verbose_name="Here you can attache files:")
    # # Contact
    # local_name = models.CharField(verbose_name="Local Contact Full Name:", max_length=64)
    # local_email = models.EmailField(verbose_name="Local Contact Email:")
    # local_phone = models.CharField(verbose_name="Local Contact Phone:", max_length=64)
    # technical_name = models.CharField(verbose_name="Technical Contact Full Name:", max_length=64)
    # technical_email = models.EmailField(verbose_name="Technical Contact Email:")
    # technical_phone = models.CharField(verbose_name="Technical Contact Phone:", max_length=64)
    # # Additional Information
    # additional_information = models.TextField(
    #     verbose_name="Please provide here all information that could be necessary to successfully perform this deployment:",
    #     null=True, max_length=64
    # )
    # # Delivery Dates
    # request_instalatioon_date = models.CharField(
    #     verbose_name="Requested install date:", max_length=64, null=True
    # )
    # go_live_date = models.CharField(verbose_name="Go-live date:", max_length=64)
    # # Number of Users
    # white_collars_num = models.IntegerField(verbose_name="Number of white collars:")
    # blue_collars_num = models.IntegerField(verbose_name="Number of blue collars:")
    # # Primary Contact
    # contact_name = models.CharField(verbose_name="Full Name:", max_length=64, null=True)
    # contact_email = models.EmailField(verbose_name="Email:", null=True)
    # contact_phone = models.CharField(verbose_name="Phone:", max_length=64, null=True)
    # # Secondary Contact
    # contact_name2 = models.CharField(verbose_name="Full Name:", max_length=64, null=True)
    # contact_email2 = models.EmailField(verbose_name="Email:", null=True)
    # contact_phone2 = models.CharField(verbose_name="Phone:", max_length=64, null=True)
    # # DMARC information(primary)
    # company_name2 = models.CharField(verbose_name="Company Name:", max_length=64, null=True)
    # building_type = models.CharField(verbose_name="Building Type:", max_length=64, null=True)
    # floor = models.IntegerField(verbose_name="Floor:", null=True)
    # site_code2 = models.CharField(verbose_name="Site Code:", max_length=64, null=True)
    # # DMARC information(secondary)
    # company_name3 = models.CharField(verbose_name="Company Name:", max_length=64, null=True)
    # building_type3 = models.CharField(verbose_name="Building Type:", max_length=64, null=True)
    # floor3 = models.IntegerField(verbose_name="Floor:", null=True, default=False)
    # site_code3 = models.CharField(verbose_name="Site Code:", max_length=64, null=True)
    # # Server Room Details
    # rack_space = models.BooleanField(choices=BOLEAN, verbose_name="Do you have a space for a least 3 rack units per router?:", null=True, default=False)
    # cooling = models.BooleanField(choices=BOLEAN, verbose_name="Is there cooling in the Server room?:", null=True, default=False)
    # power = models.BooleanField(choices=BOLEAN, verbose_name="Is there power on site?:", null=True, default=False)
    # power_before_instalation = models.BooleanField(choices=BOLEAN, verbose_name="If no will you have power on site before install date?:", null=True, default=False)
    # power_backup = models.BooleanField(choices=BOLEAN, verbose_name="Is there emergency back-up power for the equipment?:", null=True, default=False)
    # emergency_power = models.BooleanField(choices=BOLEAN, verbose_name="Do you want help with building an emergency power?:", null=True, default=False)
    # # LAN Details
    # lan_assistance2 = models.BooleanField(choices=BOLEAN, verbose_name="Help with LAN needed?:", null=True, default=False)
    # wireless = models.BooleanField(choices=BOLEAN, verbose_name="Wireless LAN?:", null=True, default=False)
    # standard_wireless = models.BooleanField(choices=BOLEAN, verbose_name="Standard Wireless?:", null=True, default=False)
    # telephone_service = models.BooleanField(choices=BOLEAN, verbose_name="Do you want to deploy telephony services?:", null=True, default=False)
    # pstn_lines = models.BooleanField(choices=BOLEAN, verbose_name="Are you using locat PSTN lines at the moment?:", null=True, default=False)
    # reason = models.CharField(verbose_name="If No: Please specify reason why?:", max_length=64, null=True, default="")

    # comment = models.ForeignKey(NocComment, on_delete=models.CASCADE)


    def __str__(self):
        return self.site_code

    def __unicode__(self):
        return self.site_code

    def get_absolute_url(self):
        return '/lbe_portal/{}'.format(self.pk)

    def get_api_url(self):
        return reverse('lbeportal-api:detail', kwargs={'pk': self.pk})
        # return 'api/lbe_portal/{}'.format(self.pk)

    # def get_markdown(self):
    #     site_code = self.site_code
    #     markdown_text = markdown(site_code)
    #     return mark_safe(markdown_text)

    # def get_absolute_url(self):
    #     return reverse("lbeportal:detail", id=self.id)



