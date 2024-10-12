# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PhotoVisibility(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, isfamily: bool=None, isfriend: bool=None, ispublic: bool=None):
        """PhotoVisibility - a model defined in OpenAPI

        :param isfamily: The isfamily of this PhotoVisibility.
        :param isfriend: The isfriend of this PhotoVisibility.
        :param ispublic: The ispublic of this PhotoVisibility.
        """
        self.openapi_types = {
            'isfamily': bool,
            'isfriend': bool,
            'ispublic': bool
        }

        self.attribute_map = {
            'isfamily': 'isfamily',
            'isfriend': 'isfriend',
            'ispublic': 'ispublic'
        }

        self._isfamily = isfamily
        self._isfriend = isfriend
        self._ispublic = ispublic

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PhotoVisibility':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Photo_visibility of this PhotoVisibility.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def isfamily(self):
        """Gets the isfamily of this PhotoVisibility.


        :return: The isfamily of this PhotoVisibility.
        :rtype: bool
        """
        return self._isfamily

    @isfamily.setter
    def isfamily(self, isfamily):
        """Sets the isfamily of this PhotoVisibility.


        :param isfamily: The isfamily of this PhotoVisibility.
        :type isfamily: bool
        """

        self._isfamily = isfamily

    @property
    def isfriend(self):
        """Gets the isfriend of this PhotoVisibility.


        :return: The isfriend of this PhotoVisibility.
        :rtype: bool
        """
        return self._isfriend

    @isfriend.setter
    def isfriend(self, isfriend):
        """Sets the isfriend of this PhotoVisibility.


        :param isfriend: The isfriend of this PhotoVisibility.
        :type isfriend: bool
        """

        self._isfriend = isfriend

    @property
    def ispublic(self):
        """Gets the ispublic of this PhotoVisibility.


        :return: The ispublic of this PhotoVisibility.
        :rtype: bool
        """
        return self._ispublic

    @ispublic.setter
    def ispublic(self, ispublic):
        """Sets the ispublic of this PhotoVisibility.


        :param ispublic: The ispublic of this PhotoVisibility.
        :type ispublic: bool
        """

        self._ispublic = ispublic
