# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VehicleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, registration_number: str=None):
        """VehicleRequest - a model defined in OpenAPI

        :param registration_number: The registration_number of this VehicleRequest.
        """
        self.openapi_types = {
            'registration_number': str
        }

        self.attribute_map = {
            'registration_number': 'registrationNumber'
        }

        self._registration_number = registration_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VehicleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VehicleRequest of this VehicleRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def registration_number(self):
        """Gets the registration_number of this VehicleRequest.


        :return: The registration_number of this VehicleRequest.
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this VehicleRequest.


        :param registration_number: The registration_number of this VehicleRequest.
        :type registration_number: str
        """

        self._registration_number = registration_number
