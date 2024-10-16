# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Language(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, language_name: str=None, previous_count: int=None):
        """Language - a model defined in OpenAPI

        :param count: The count of this Language.
        :param language_name: The language_name of this Language.
        :param previous_count: The previous_count of this Language.
        """
        self.openapi_types = {
            'count': int,
            'language_name': str,
            'previous_count': int
        }

        self.attribute_map = {
            'count': 'count',
            'language_name': 'language_name',
            'previous_count': 'previous_count'
        }

        self._count = count
        self._language_name = language_name
        self._previous_count = previous_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Language':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Language of this Language.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this Language.

        Count current of language.

        :return: The count of this Language.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Language.

        Count current of language.

        :param count: The count of this Language.
        :type count: int
        """

        self._count = count

    @property
    def language_name(self):
        """Gets the language_name of this Language.

        Language's name.

        :return: The language_name of this Language.
        :rtype: str
        """
        return self._language_name

    @language_name.setter
    def language_name(self, language_name):
        """Sets the language_name of this Language.

        Language's name.

        :param language_name: The language_name of this Language.
        :type language_name: str
        """

        self._language_name = language_name

    @property
    def previous_count(self):
        """Gets the previous_count of this Language.

        Count of previous lanugage.

        :return: The previous_count of this Language.
        :rtype: int
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this Language.

        Count of previous lanugage.

        :param previous_count: The previous_count of this Language.
        :type previous_count: int
        """

        self._previous_count = previous_count
