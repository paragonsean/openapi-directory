# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.venues_entity_type import VenuesEntityType
from openapi_server import util


class VenuesEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alternative_labels: List[str]=None, city: str=None, country_code: str=None, creation_timestamp: int=None, first_address: str=None, id: int=None, label: str=None, last_update_timestamp: int=None, major_city: str=None, second_address: str=None, type: VenuesEntityType=None, zip_code: str=None):
        """VenuesEntity - a model defined in OpenAPI

        :param alternative_labels: The alternative_labels of this VenuesEntity.
        :param city: The city of this VenuesEntity.
        :param country_code: The country_code of this VenuesEntity.
        :param creation_timestamp: The creation_timestamp of this VenuesEntity.
        :param first_address: The first_address of this VenuesEntity.
        :param id: The id of this VenuesEntity.
        :param label: The label of this VenuesEntity.
        :param last_update_timestamp: The last_update_timestamp of this VenuesEntity.
        :param major_city: The major_city of this VenuesEntity.
        :param second_address: The second_address of this VenuesEntity.
        :param type: The type of this VenuesEntity.
        :param zip_code: The zip_code of this VenuesEntity.
        """
        self.openapi_types = {
            'alternative_labels': List[str],
            'city': str,
            'country_code': str,
            'creation_timestamp': int,
            'first_address': str,
            'id': int,
            'label': str,
            'last_update_timestamp': int,
            'major_city': str,
            'second_address': str,
            'type': VenuesEntityType,
            'zip_code': str
        }

        self.attribute_map = {
            'alternative_labels': 'alternative_labels',
            'city': 'city',
            'country_code': 'country_code',
            'creation_timestamp': 'creation_timestamp',
            'first_address': 'first_address',
            'id': 'id',
            'label': 'label',
            'last_update_timestamp': 'last_update_timestamp',
            'major_city': 'major_city',
            'second_address': 'second_address',
            'type': 'type',
            'zip_code': 'zip_code'
        }

        self._alternative_labels = alternative_labels
        self._city = city
        self._country_code = country_code
        self._creation_timestamp = creation_timestamp
        self._first_address = first_address
        self._id = id
        self._label = label
        self._last_update_timestamp = last_update_timestamp
        self._major_city = major_city
        self._second_address = second_address
        self._type = type
        self._zip_code = zip_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VenuesEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VenuesEntity of this VenuesEntity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alternative_labels(self):
        """Gets the alternative_labels of this VenuesEntity.

        Array of alternative/old names of the venue.

        :return: The alternative_labels of this VenuesEntity.
        :rtype: List[str]
        """
        return self._alternative_labels

    @alternative_labels.setter
    def alternative_labels(self, alternative_labels):
        """Sets the alternative_labels of this VenuesEntity.

        Array of alternative/old names of the venue.

        :param alternative_labels: The alternative_labels of this VenuesEntity.
        :type alternative_labels: List[str]
        """

        self._alternative_labels = alternative_labels

    @property
    def city(self):
        """Gets the city of this VenuesEntity.

        City in which the venue is.

        :return: The city of this VenuesEntity.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this VenuesEntity.

        City in which the venue is.

        :param city: The city of this VenuesEntity.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this VenuesEntity.

        Country in which the venue is (<a href='https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3'>ISO 3166-1 alpha-3 code</a>).

        :return: The country_code of this VenuesEntity.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this VenuesEntity.

        Country in which the venue is (<a href='https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3'>ISO 3166-1 alpha-3 code</a>).

        :param country_code: The country_code of this VenuesEntity.
        :type country_code: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")

        self._country_code = country_code

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this VenuesEntity.

        Timestamp for when the venue was created in the customer's database.

        :return: The creation_timestamp of this VenuesEntity.
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this VenuesEntity.

        Timestamp for when the venue was created in the customer's database.

        :param creation_timestamp: The creation_timestamp of this VenuesEntity.
        :type creation_timestamp: int
        """
        if creation_timestamp is None:
            raise ValueError("Invalid value for `creation_timestamp`, must not be `None`")

        self._creation_timestamp = creation_timestamp

    @property
    def first_address(self):
        """Gets the first_address of this VenuesEntity.

        First address field of the venue.

        :return: The first_address of this VenuesEntity.
        :rtype: str
        """
        return self._first_address

    @first_address.setter
    def first_address(self, first_address):
        """Sets the first_address of this VenuesEntity.

        First address field of the venue.

        :param first_address: The first_address of this VenuesEntity.
        :type first_address: str
        """
        if first_address is None:
            raise ValueError("Invalid value for `first_address`, must not be `None`")

        self._first_address = first_address

    @property
    def id(self):
        """Gets the id of this VenuesEntity.

        Unique ID of the venue.

        :return: The id of this VenuesEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VenuesEntity.

        Unique ID of the venue.

        :param id: The id of this VenuesEntity.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def label(self):
        """Gets the label of this VenuesEntity.

        Name of the venue.

        :return: The label of this VenuesEntity.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VenuesEntity.

        Name of the venue.

        :param label: The label of this VenuesEntity.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this VenuesEntity.

        Timestamp for when the venue was last updated in the customer's database.

        :return: The last_update_timestamp of this VenuesEntity.
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this VenuesEntity.

        Timestamp for when the venue was last updated in the customer's database.

        :param last_update_timestamp: The last_update_timestamp of this VenuesEntity.
        :type last_update_timestamp: int
        """
        if last_update_timestamp is None:
            raise ValueError("Invalid value for `last_update_timestamp`, must not be `None`")

        self._last_update_timestamp = last_update_timestamp

    @property
    def major_city(self):
        """Gets the major_city of this VenuesEntity.

        Major city or metropolitan area the venue belongs to.

        :return: The major_city of this VenuesEntity.
        :rtype: str
        """
        return self._major_city

    @major_city.setter
    def major_city(self, major_city):
        """Sets the major_city of this VenuesEntity.

        Major city or metropolitan area the venue belongs to.

        :param major_city: The major_city of this VenuesEntity.
        :type major_city: str
        """
        if major_city is None:
            raise ValueError("Invalid value for `major_city`, must not be `None`")

        self._major_city = major_city

    @property
    def second_address(self):
        """Gets the second_address of this VenuesEntity.

        Second address field of the venue.

        :return: The second_address of this VenuesEntity.
        :rtype: str
        """
        return self._second_address

    @second_address.setter
    def second_address(self, second_address):
        """Sets the second_address of this VenuesEntity.

        Second address field of the venue.

        :param second_address: The second_address of this VenuesEntity.
        :type second_address: str
        """
        if second_address is None:
            raise ValueError("Invalid value for `second_address`, must not be `None`")

        self._second_address = second_address

    @property
    def type(self):
        """Gets the type of this VenuesEntity.


        :return: The type of this VenuesEntity.
        :rtype: VenuesEntityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VenuesEntity.


        :param type: The type of this VenuesEntity.
        :type type: VenuesEntityType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def zip_code(self):
        """Gets the zip_code of this VenuesEntity.

        ZIP code of the venue.

        :return: The zip_code of this VenuesEntity.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this VenuesEntity.

        ZIP code of the venue.

        :param zip_code: The zip_code of this VenuesEntity.
        :type zip_code: str
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")

        self._zip_code = zip_code
