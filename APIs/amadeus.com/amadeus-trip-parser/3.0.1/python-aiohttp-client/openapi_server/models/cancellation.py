# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.description import Description
from openapi_server import util


class Cancellation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: Description=None):
        """Cancellation - a model defined in OpenAPI

        :param description: The description of this Cancellation.
        """
        self.openapi_types = {
            'description': Description
        }

        self.attribute_map = {
            'description': 'description'
        }

        self._description = description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Cancellation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The cancellation of this Cancellation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Cancellation.


        :return: The description of this Cancellation.
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Cancellation.


        :param description: The description of this Cancellation.
        :type description: Description
        """

        self._description = description
