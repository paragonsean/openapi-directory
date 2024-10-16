# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Flag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _date: datetime=None, email: str=None, id: str=None, notes: str=None, type: str=None):
        """Flag - a model defined in OpenAPI

        :param _date: The _date of this Flag.
        :param email: The email of this Flag.
        :param id: The id of this Flag.
        :param notes: The notes of this Flag.
        :param type: The type of this Flag.
        """
        self.openapi_types = {
            '_date': datetime,
            'email': str,
            'id': str,
            'notes': str,
            'type': str
        }

        self.attribute_map = {
            '_date': 'date',
            'email': 'email',
            'id': 'id',
            'notes': 'notes',
            'type': 'type'
        }

        self.__date = _date
        self._email = email
        self._id = id
        self._notes = notes
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Flag':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Flag of this Flag.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self):
        """Gets the _date of this Flag.


        :return: The _date of this Flag.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Flag.


        :param _date: The _date of this Flag.
        :type _date: datetime
        """

        self.__date = _date

    @property
    def email(self):
        """Gets the email of this Flag.


        :return: The email of this Flag.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Flag.


        :param email: The email of this Flag.
        :type email: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this Flag.


        :return: The id of this Flag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flag.


        :param id: The id of this Flag.
        :type id: str
        """

        self._id = id

    @property
    def notes(self):
        """Gets the notes of this Flag.


        :return: The notes of this Flag.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Flag.


        :param notes: The notes of this Flag.
        :type notes: str
        """

        self._notes = notes

    @property
    def type(self):
        """Gets the type of this Flag.


        :return: The type of this Flag.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Flag.


        :param type: The type of this Flag.
        :type type: str
        """

        self._type = type
