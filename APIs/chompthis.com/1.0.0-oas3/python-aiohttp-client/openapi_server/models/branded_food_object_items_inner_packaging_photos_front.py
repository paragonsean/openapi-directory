# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BrandedFoodObjectItemsInnerPackagingPhotosFront(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display: str=None, small: str=None, thumb: str=None):
        """BrandedFoodObjectItemsInnerPackagingPhotosFront - a model defined in OpenAPI

        :param display: The display of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :param small: The small of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :param thumb: The thumb of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        """
        self.openapi_types = {
            'display': str,
            'small': str,
            'thumb': str
        }

        self.attribute_map = {
            'display': 'display',
            'small': 'small',
            'thumb': 'thumb'
        }

        self._display = display
        self._small = small
        self._thumb = thumb

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BrandedFoodObjectItemsInnerPackagingPhotosFront':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BrandedFoodObject_items_inner_packaging_photos_front of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display(self):
        """Gets the display of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Full-sized photo of the front of this item's packaging

        :return: The display of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Full-sized photo of the front of this item's packaging

        :param display: The display of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :type display: str
        """

        self._display = display

    @property
    def small(self):
        """Gets the small of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Small photo of the front of this item's packaging

        :return: The small of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :rtype: str
        """
        return self._small

    @small.setter
    def small(self, small):
        """Sets the small of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Small photo of the front of this item's packaging

        :param small: The small of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :type small: str
        """

        self._small = small

    @property
    def thumb(self):
        """Gets the thumb of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Thumbnail photo of the front of this item's packaging

        :return: The thumb of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this BrandedFoodObjectItemsInnerPackagingPhotosFront.

        Thumbnail photo of the front of this item's packaging

        :param thumb: The thumb of this BrandedFoodObjectItemsInnerPackagingPhotosFront.
        :type thumb: str
        """

        self._thumb = thumb
