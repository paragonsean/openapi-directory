# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MemberLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, free_form: str=None):
        """MemberLocation - a model defined in OpenAPI

        :param free_form: The free_form of this MemberLocation.
        """
        self.openapi_types = {
            'free_form': str
        }

        self.attribute_map = {
            'free_form': 'free_form'
        }

        self._free_form = free_form

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MemberLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Member_location of this MemberLocation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def free_form(self):
        """Gets the free_form of this MemberLocation.


        :return: The free_form of this MemberLocation.
        :rtype: str
        """
        return self._free_form

    @free_form.setter
    def free_form(self, free_form):
        """Sets the free_form of this MemberLocation.


        :param free_form: The free_form of this MemberLocation.
        :type free_form: str
        """

        self._free_form = free_form
