# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.traveler_type import TravelerType
from openapi_server import util


class Traveler(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, associated_adult_id: str=None, id: str=None, traveler_type: TravelerType=None):
        """Traveler - a model defined in OpenAPI

        :param associated_adult_id: The associated_adult_id of this Traveler.
        :param id: The id of this Traveler.
        :param traveler_type: The traveler_type of this Traveler.
        """
        self.openapi_types = {
            'associated_adult_id': str,
            'id': str,
            'traveler_type': TravelerType
        }

        self.attribute_map = {
            'associated_adult_id': 'associatedAdultId',
            'id': 'id',
            'traveler_type': 'travelerType'
        }

        self._associated_adult_id = associated_adult_id
        self._id = id
        self._traveler_type = traveler_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Traveler':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Traveler of this Traveler.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associated_adult_id(self):
        """Gets the associated_adult_id of this Traveler.

        if type=\"HELD_INFANT\", corresponds to the adult travelers's id who will share the seat

        :return: The associated_adult_id of this Traveler.
        :rtype: str
        """
        return self._associated_adult_id

    @associated_adult_id.setter
    def associated_adult_id(self, associated_adult_id):
        """Sets the associated_adult_id of this Traveler.

        if type=\"HELD_INFANT\", corresponds to the adult travelers's id who will share the seat

        :param associated_adult_id: The associated_adult_id of this Traveler.
        :type associated_adult_id: str
        """

        self._associated_adult_id = associated_adult_id

    @property
    def id(self):
        """Gets the id of this Traveler.


        :return: The id of this Traveler.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Traveler.


        :param id: The id of this Traveler.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def traveler_type(self):
        """Gets the traveler_type of this Traveler.


        :return: The traveler_type of this Traveler.
        :rtype: TravelerType
        """
        return self._traveler_type

    @traveler_type.setter
    def traveler_type(self, traveler_type):
        """Sets the traveler_type of this Traveler.


        :param traveler_type: The traveler_type of this Traveler.
        :type traveler_type: TravelerType
        """
        if traveler_type is None:
            raise ValueError("Invalid value for `traveler_type`, must not be `None`")

        self._traveler_type = traveler_type
