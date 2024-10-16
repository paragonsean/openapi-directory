# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Countries(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: str=None, currency_id: str=None, deleted: str=None, id: str=None, identifier: str=None, language_id: str=None, modified: str=None, name: str=None, phone_code: str=None, time_zone: str=None):
        """Countries - a model defined in OpenAPI

        :param created: The created of this Countries.
        :param currency_id: The currency_id of this Countries.
        :param deleted: The deleted of this Countries.
        :param id: The id of this Countries.
        :param identifier: The identifier of this Countries.
        :param language_id: The language_id of this Countries.
        :param modified: The modified of this Countries.
        :param name: The name of this Countries.
        :param phone_code: The phone_code of this Countries.
        :param time_zone: The time_zone of this Countries.
        """
        self.openapi_types = {
            'created': str,
            'currency_id': str,
            'deleted': str,
            'id': str,
            'identifier': str,
            'language_id': str,
            'modified': str,
            'name': str,
            'phone_code': str,
            'time_zone': str
        }

        self.attribute_map = {
            'created': 'created',
            'currency_id': 'currency_id',
            'deleted': 'deleted',
            'id': 'id',
            'identifier': 'identifier',
            'language_id': 'language_id',
            'modified': 'modified',
            'name': 'name',
            'phone_code': 'phone_code',
            'time_zone': 'time_zone'
        }

        self._created = created
        self._currency_id = currency_id
        self._deleted = deleted
        self._id = id
        self._identifier = identifier
        self._language_id = language_id
        self._modified = modified
        self._name = name
        self._phone_code = phone_code
        self._time_zone = time_zone

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Countries':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Countries of this Countries.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this Countries.


        :return: The created of this Countries.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Countries.


        :param created: The created of this Countries.
        :type created: str
        """

        self._created = created

    @property
    def currency_id(self):
        """Gets the currency_id of this Countries.


        :return: The currency_id of this Countries.
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Countries.


        :param currency_id: The currency_id of this Countries.
        :type currency_id: str
        """

        self._currency_id = currency_id

    @property
    def deleted(self):
        """Gets the deleted of this Countries.

        Only present if it's a deleted object

        :return: The deleted of this Countries.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Countries.

        Only present if it's a deleted object

        :param deleted: The deleted of this Countries.
        :type deleted: str
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this Countries.


        :return: The id of this Countries.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Countries.


        :param id: The id of this Countries.
        :type id: str
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this Countries.


        :return: The identifier of this Countries.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Countries.


        :param identifier: The identifier of this Countries.
        :type identifier: str
        """
        if identifier is not None and len(identifier) > 255:
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `255`")

        self._identifier = identifier

    @property
    def language_id(self):
        """Gets the language_id of this Countries.


        :return: The language_id of this Countries.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """Sets the language_id of this Countries.


        :param language_id: The language_id of this Countries.
        :type language_id: str
        """

        self._language_id = language_id

    @property
    def modified(self):
        """Gets the modified of this Countries.


        :return: The modified of this Countries.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Countries.


        :param modified: The modified of this Countries.
        :type modified: str
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Countries.


        :return: The name of this Countries.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Countries.


        :param name: The name of this Countries.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")

        self._name = name

    @property
    def phone_code(self):
        """Gets the phone_code of this Countries.


        :return: The phone_code of this Countries.
        :rtype: str
        """
        return self._phone_code

    @phone_code.setter
    def phone_code(self, phone_code):
        """Sets the phone_code of this Countries.


        :param phone_code: The phone_code of this Countries.
        :type phone_code: str
        """
        if phone_code is not None and len(phone_code) > 10:
            raise ValueError("Invalid value for `phone_code`, length must be less than or equal to `10`")

        self._phone_code = phone_code

    @property
    def time_zone(self):
        """Gets the time_zone of this Countries.


        :return: The time_zone of this Countries.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Countries.


        :param time_zone: The time_zone of this Countries.
        :type time_zone: str
        """
        if time_zone is not None and len(time_zone) > 255:
            raise ValueError("Invalid value for `time_zone`, length must be less than or equal to `255`")

        self._time_zone = time_zone
