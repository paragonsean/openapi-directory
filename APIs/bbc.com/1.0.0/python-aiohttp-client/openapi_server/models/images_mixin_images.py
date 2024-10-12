# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.images_mixin_images_image import ImagesMixinImagesImage
from openapi_server import util


class ImagesMixinImages(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image: ImagesMixinImagesImage=None):
        """ImagesMixinImages - a model defined in OpenAPI

        :param image: The image of this ImagesMixinImages.
        """
        self.openapi_types = {
            'image': ImagesMixinImagesImage
        }

        self.attribute_map = {
            'image': 'image'
        }

        self._image = image

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImagesMixinImages':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The images_mixin_images of this ImagesMixinImages.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self):
        """Gets the image of this ImagesMixinImages.


        :return: The image of this ImagesMixinImages.
        :rtype: ImagesMixinImagesImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImagesMixinImages.


        :param image: The image of this ImagesMixinImages.
        :type image: ImagesMixinImagesImage
        """

        self._image = image
