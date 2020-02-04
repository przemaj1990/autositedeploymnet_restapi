from django.db import models
# Create your models here.
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

# class CommentManager(models.Manager):
#     def filter_by_instance(self, instance):
#         content_type = ContentType.objects.get_for_model(SiteVendor)
#         obj_id = instance.id
#         qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
#         return qs


class NocComment(models.Model):
    content = models.TextField(verbose_name="Comment from NOC team:")
    user = models.CharField(verbose_name="User:", max_length=64)
    site = models.ForeignKey('lbeportal.SiteVendor', on_delete=models.CASCADE, related_name='comment')

    # Below the mandatory fields for generic relation
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()

    def __str__(self):
        return self.content

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type
    


