# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RetrieveHealthIdPayloadResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, health_id: str=None, health_id_number: str=None):
        """RetrieveHealthIdPayloadResponse - a model defined in OpenAPI

        :param health_id: The health_id of this RetrieveHealthIdPayloadResponse.
        :param health_id_number: The health_id_number of this RetrieveHealthIdPayloadResponse.
        """
        self.openapi_types = {
            'health_id': str,
            'health_id_number': str
        }

        self.attribute_map = {
            'health_id': 'healthId',
            'health_id_number': 'healthIdNumber'
        }

        self._health_id = health_id
        self._health_id_number = health_id_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RetrieveHealthIdPayloadResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RetrieveHealthIdPayloadResponse of this RetrieveHealthIdPayloadResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def health_id(self):
        """Gets the health_id of this RetrieveHealthIdPayloadResponse.


        :return: The health_id of this RetrieveHealthIdPayloadResponse.
        :rtype: str
        """
        return self._health_id

    @health_id.setter
    def health_id(self, health_id):
        """Sets the health_id of this RetrieveHealthIdPayloadResponse.


        :param health_id: The health_id of this RetrieveHealthIdPayloadResponse.
        :type health_id: str
        """

        self._health_id = health_id

    @property
    def health_id_number(self):
        """Gets the health_id_number of this RetrieveHealthIdPayloadResponse.


        :return: The health_id_number of this RetrieveHealthIdPayloadResponse.
        :rtype: str
        """
        return self._health_id_number

    @health_id_number.setter
    def health_id_number(self, health_id_number):
        """Sets the health_id_number of this RetrieveHealthIdPayloadResponse.


        :param health_id_number: The health_id_number of this RetrieveHealthIdPayloadResponse.
        :type health_id_number: str
        """

        self._health_id_number = health_id_number
