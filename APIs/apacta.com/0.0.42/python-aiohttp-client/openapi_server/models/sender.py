# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Sender(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city_id: str=None, created: str=None, created_by_id: str=None, cvr: str=None, deleted: str=None, email: str=None, id: str=None, language_id: str=None, modified: str=None, name: str=None, phone: str=None, phone_countrycode: str=None, street_name: str=None, website: str=None):
        """Sender - a model defined in OpenAPI

        :param city_id: The city_id of this Sender.
        :param created: The created of this Sender.
        :param created_by_id: The created_by_id of this Sender.
        :param cvr: The cvr of this Sender.
        :param deleted: The deleted of this Sender.
        :param email: The email of this Sender.
        :param id: The id of this Sender.
        :param language_id: The language_id of this Sender.
        :param modified: The modified of this Sender.
        :param name: The name of this Sender.
        :param phone: The phone of this Sender.
        :param phone_countrycode: The phone_countrycode of this Sender.
        :param street_name: The street_name of this Sender.
        :param website: The website of this Sender.
        """
        self.openapi_types = {
            'city_id': str,
            'created': str,
            'created_by_id': str,
            'cvr': str,
            'deleted': str,
            'email': str,
            'id': str,
            'language_id': str,
            'modified': str,
            'name': str,
            'phone': str,
            'phone_countrycode': str,
            'street_name': str,
            'website': str
        }

        self.attribute_map = {
            'city_id': 'city_id',
            'created': 'created',
            'created_by_id': 'created_by_id',
            'cvr': 'cvr',
            'deleted': 'deleted',
            'email': 'email',
            'id': 'id',
            'language_id': 'language_id',
            'modified': 'modified',
            'name': 'name',
            'phone': 'phone',
            'phone_countrycode': 'phone_countrycode',
            'street_name': 'street_name',
            'website': 'website'
        }

        self._city_id = city_id
        self._created = created
        self._created_by_id = created_by_id
        self._cvr = cvr
        self._deleted = deleted
        self._email = email
        self._id = id
        self._language_id = language_id
        self._modified = modified
        self._name = name
        self._phone = phone
        self._phone_countrycode = phone_countrycode
        self._street_name = street_name
        self._website = website

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Sender':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Sender of this Sender.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city_id(self):
        """Gets the city_id of this Sender.


        :return: The city_id of this Sender.
        :rtype: str
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        """Sets the city_id of this Sender.


        :param city_id: The city_id of this Sender.
        :type city_id: str
        """

        self._city_id = city_id

    @property
    def created(self):
        """Gets the created of this Sender.


        :return: The created of this Sender.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Sender.


        :param created: The created of this Sender.
        :type created: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """Gets the created_by_id of this Sender.

        Read-only

        :return: The created_by_id of this Sender.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this Sender.

        Read-only

        :param created_by_id: The created_by_id of this Sender.
        :type created_by_id: str
        """

        self._created_by_id = created_by_id

    @property
    def cvr(self):
        """Gets the cvr of this Sender.


        :return: The cvr of this Sender.
        :rtype: str
        """
        return self._cvr

    @cvr.setter
    def cvr(self, cvr):
        """Sets the cvr of this Sender.


        :param cvr: The cvr of this Sender.
        :type cvr: str
        """
        if cvr is not None and len(cvr) > 255:
            raise ValueError("Invalid value for `cvr`, length must be less than or equal to `255`")

        self._cvr = cvr

    @property
    def deleted(self):
        """Gets the deleted of this Sender.

        Only present if it's a deleted object

        :return: The deleted of this Sender.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Sender.

        Only present if it's a deleted object

        :param deleted: The deleted of this Sender.
        :type deleted: str
        """

        self._deleted = deleted

    @property
    def email(self):
        """Gets the email of this Sender.


        :return: The email of this Sender.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Sender.


        :param email: The email of this Sender.
        :type email: str
        """
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")

        self._email = email

    @property
    def id(self):
        """Gets the id of this Sender.


        :return: The id of this Sender.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sender.


        :param id: The id of this Sender.
        :type id: str
        """

        self._id = id

    @property
    def language_id(self):
        """Gets the language_id of this Sender.


        :return: The language_id of this Sender.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """Sets the language_id of this Sender.


        :param language_id: The language_id of this Sender.
        :type language_id: str
        """

        self._language_id = language_id

    @property
    def modified(self):
        """Gets the modified of this Sender.


        :return: The modified of this Sender.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Sender.


        :param modified: The modified of this Sender.
        :type modified: str
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Sender.


        :return: The name of this Sender.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sender.


        :param name: The name of this Sender.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Sender.

        Format like eg. `28680133` or `046158971404`

        :return: The phone of this Sender.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Sender.

        Format like eg. `28680133` or `046158971404`

        :param phone: The phone of this Sender.
        :type phone: str
        """
        if phone is not None and len(phone) > 32:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `32`")

        self._phone = phone

    @property
    def phone_countrycode(self):
        """Gets the phone_countrycode of this Sender.

        Format like eg. `45` or `49`

        :return: The phone_countrycode of this Sender.
        :rtype: str
        """
        return self._phone_countrycode

    @phone_countrycode.setter
    def phone_countrycode(self, phone_countrycode):
        """Sets the phone_countrycode of this Sender.

        Format like eg. `45` or `49`

        :param phone_countrycode: The phone_countrycode of this Sender.
        :type phone_countrycode: str
        """
        if phone_countrycode is not None and len(phone_countrycode) > 3:
            raise ValueError("Invalid value for `phone_countrycode`, length must be less than or equal to `3`")

        self._phone_countrycode = phone_countrycode

    @property
    def street_name(self):
        """Gets the street_name of this Sender.


        :return: The street_name of this Sender.
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Sender.


        :param street_name: The street_name of this Sender.
        :type street_name: str
        """
        if street_name is not None and len(street_name) > 255:
            raise ValueError("Invalid value for `street_name`, length must be less than or equal to `255`")

        self._street_name = street_name

    @property
    def website(self):
        """Gets the website of this Sender.


        :return: The website of this Sender.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Sender.


        :param website: The website of this Sender.
        :type website: str
        """
        if website is not None and len(website) > 255:
            raise ValueError("Invalid value for `website`, length must be less than or equal to `255`")

        self._website = website
