from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from django.utils import timezone

@python_2_unicode_compatible
class Category(models.Model):
    """
    A class representing a category to which photos belong.
    """

    # We want the correct pluralisation on the admin site.
    class Meta:
        verbose_name_plural = "categories"

    category_title = models.CharField(max_length=20,
                                      help_text="The name of the category.")
    category_date = models.DateTimeField('Date category added', 
                                      default=timezone.now)

    def __str__(self):
        return self.category_title

@python_2_unicode_compatible
class Photo(models.Model):
    """
    A class representing a photo.
    """

    photo_title = models.CharField(max_length=30, 
                                   help_text="Enter the title of the photo.")

    photo_description = models.TextField(max_length=500,
                                         help_text="Enter a description for the photo.")

    photo_date = models.DateTimeField('Date',
                                      help_text="When was the photo taken?")

    photo_full = models.ImageField("Photo",
                                   upload_to='full',
                                   help_text="The full size image.")

    # Requires PIL/Pillow and django-imagekit
    photo_small = ImageSpecField(source='photo_full',
                                 processors=[SmartResize(450, 300)],
                                 format='JPEG',
                                 options={'quality': 60})
                                 # quality is (worst) 1 to 100 (best)

    """
       * A Photo can be in more than one Category
       * A Category can have more than one Photo
    """
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.photo_title