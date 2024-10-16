# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TestGetDeviceConfigurations200ResponseInnerImage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, full: str=None, thumb: str=None):
        """TestGetDeviceConfigurations200ResponseInnerImage - a model defined in OpenAPI

        :param full: The full of this TestGetDeviceConfigurations200ResponseInnerImage.
        :param thumb: The thumb of this TestGetDeviceConfigurations200ResponseInnerImage.
        """
        self.openapi_types = {
            'full': str,
            'thumb': str
        }

        self.attribute_map = {
            'full': 'full',
            'thumb': 'thumb'
        }

        self._full = full
        self._thumb = thumb

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestGetDeviceConfigurations200ResponseInnerImage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The test_getDeviceConfigurations_200_response_inner_image of this TestGetDeviceConfigurations200ResponseInnerImage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def full(self):
        """Gets the full of this TestGetDeviceConfigurations200ResponseInnerImage.


        :return: The full of this TestGetDeviceConfigurations200ResponseInnerImage.
        :rtype: str
        """
        return self._full

    @full.setter
    def full(self, full):
        """Sets the full of this TestGetDeviceConfigurations200ResponseInnerImage.


        :param full: The full of this TestGetDeviceConfigurations200ResponseInnerImage.
        :type full: str
        """

        self._full = full

    @property
    def thumb(self):
        """Gets the thumb of this TestGetDeviceConfigurations200ResponseInnerImage.


        :return: The thumb of this TestGetDeviceConfigurations200ResponseInnerImage.
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this TestGetDeviceConfigurations200ResponseInnerImage.


        :param thumb: The thumb of this TestGetDeviceConfigurations200ResponseInnerImage.
        :type thumb: str
        """

        self._thumb = thumb
