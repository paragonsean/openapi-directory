# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.alternate_images_mixin_alternate_images_alternate_image_inner_alternate_images_alternate_image_inner import AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner
from openapi_server import util


class AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alternate_image: List[AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner]=None):
        """AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages - a model defined in OpenAPI

        :param alternate_image: The alternate_image of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.
        """
        self.openapi_types = {
            'alternate_image': List[AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner]
        }

        self.attribute_map = {
            'alternate_image': 'alternate_image'
        }

        self._alternate_image = alternate_image

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The alternate_images_mixin_alternate_images_alternate_image_inner_alternate_images of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alternate_image(self):
        """Gets the alternate_image of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.


        :return: The alternate_image of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.
        :rtype: List[AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner]
        """
        return self._alternate_image

    @alternate_image.setter
    def alternate_image(self, alternate_image):
        """Sets the alternate_image of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.


        :param alternate_image: The alternate_image of this AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImages.
        :type alternate_image: List[AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner]
        """

        self._alternate_image = alternate_image
