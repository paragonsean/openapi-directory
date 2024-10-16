# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class SearchOverPlayers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birthday: str=None, first_name: str=None, hometown: str=None, last_name: str=None, name: str=None, nationality: str=None, role: str=None, slug: str=None):
        """SearchOverPlayers - a model defined in OpenAPI

        :param birthday: The birthday of this SearchOverPlayers.
        :param first_name: The first_name of this SearchOverPlayers.
        :param hometown: The hometown of this SearchOverPlayers.
        :param last_name: The last_name of this SearchOverPlayers.
        :param name: The name of this SearchOverPlayers.
        :param nationality: The nationality of this SearchOverPlayers.
        :param role: The role of this SearchOverPlayers.
        :param slug: The slug of this SearchOverPlayers.
        """
        self.openapi_types = {
            'birthday': str,
            'first_name': str,
            'hometown': str,
            'last_name': str,
            'name': str,
            'nationality': str,
            'role': str,
            'slug': str
        }

        self.attribute_map = {
            'birthday': 'birthday',
            'first_name': 'first_name',
            'hometown': 'hometown',
            'last_name': 'last_name',
            'name': 'name',
            'nationality': 'nationality',
            'role': 'role',
            'slug': 'slug'
        }

        self._birthday = birthday
        self._first_name = first_name
        self._hometown = hometown
        self._last_name = last_name
        self._name = name
        self._nationality = nationality
        self._role = role
        self._slug = slug

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SearchOverPlayers':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The search_over_Players of this SearchOverPlayers.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birthday(self):
        """Gets the birthday of this SearchOverPlayers.

        Not present if the client did not subscribe to the appropriate plan.

        :return: The birthday of this SearchOverPlayers.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this SearchOverPlayers.

        Not present if the client did not subscribe to the appropriate plan.

        :param birthday: The birthday of this SearchOverPlayers.
        :type birthday: str
        """

        self._birthday = birthday

    @property
    def first_name(self):
        """Gets the first_name of this SearchOverPlayers.


        :return: The first_name of this SearchOverPlayers.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SearchOverPlayers.


        :param first_name: The first_name of this SearchOverPlayers.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def hometown(self):
        """Gets the hometown of this SearchOverPlayers.


        :return: The hometown of this SearchOverPlayers.
        :rtype: str
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this SearchOverPlayers.


        :param hometown: The hometown of this SearchOverPlayers.
        :type hometown: str
        """

        self._hometown = hometown

    @property
    def last_name(self):
        """Gets the last_name of this SearchOverPlayers.


        :return: The last_name of this SearchOverPlayers.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SearchOverPlayers.


        :param last_name: The last_name of this SearchOverPlayers.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this SearchOverPlayers.


        :return: The name of this SearchOverPlayers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchOverPlayers.


        :param name: The name of this SearchOverPlayers.
        :type name: str
        """

        self._name = name

    @property
    def nationality(self):
        """Gets the nationality of this SearchOverPlayers.


        :return: The nationality of this SearchOverPlayers.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this SearchOverPlayers.


        :param nationality: The nationality of this SearchOverPlayers.
        :type nationality: str
        """

        self._nationality = nationality

    @property
    def role(self):
        """Gets the role of this SearchOverPlayers.


        :return: The role of this SearchOverPlayers.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SearchOverPlayers.


        :param role: The role of this SearchOverPlayers.
        :type role: str
        """

        self._role = role

    @property
    def slug(self):
        """Gets the slug of this SearchOverPlayers.


        :return: The slug of this SearchOverPlayers.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SearchOverPlayers.


        :param slug: The slug of this SearchOverPlayers.
        :type slug: str
        """
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")
        if slug is not None and not re.search(r'^[a-z0-9_-]+$', slug):
            raise ValueError("Invalid value for `slug`, must be a follow pattern or equal to `/^[a-z0-9_-]+$/`")

        self._slug = slug
