# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PatientAuthRequester(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, type: str=None):
        """PatientAuthRequester - a model defined in OpenAPI

        :param id: The id of this PatientAuthRequester.
        :param type: The type of this PatientAuthRequester.
        """
        self.openapi_types = {
            'id': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type'
        }

        self._id = id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientAuthRequester':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientAuthRequester of this PatientAuthRequester.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PatientAuthRequester.


        :return: The id of this PatientAuthRequester.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatientAuthRequester.


        :param id: The id of this PatientAuthRequester.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def type(self):
        """Gets the type of this PatientAuthRequester.


        :return: The type of this PatientAuthRequester.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatientAuthRequester.


        :param type: The type of this PatientAuthRequester.
        :type type: str
        """
        allowed_values = ["HIP", "HIU"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
