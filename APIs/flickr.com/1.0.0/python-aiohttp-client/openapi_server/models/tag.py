# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Tag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content: str=None, author: str=None, authorname: str=None, id: str=None, machine_tag: bool=None, raw: str=None):
        """Tag - a model defined in OpenAPI

        :param content: The content of this Tag.
        :param author: The author of this Tag.
        :param authorname: The authorname of this Tag.
        :param id: The id of this Tag.
        :param machine_tag: The machine_tag of this Tag.
        :param raw: The raw of this Tag.
        """
        self.openapi_types = {
            'content': str,
            'author': str,
            'authorname': str,
            'id': str,
            'machine_tag': bool,
            'raw': str
        }

        self.attribute_map = {
            'content': '_content',
            'author': 'author',
            'authorname': 'authorname',
            'id': 'id',
            'machine_tag': 'machine_tag',
            'raw': 'raw'
        }

        self._content = content
        self._author = author
        self._authorname = authorname
        self._id = id
        self._machine_tag = machine_tag
        self._raw = raw

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Tag of this Tag.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self):
        """Gets the content of this Tag.


        :return: The content of this Tag.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Tag.


        :param content: The content of this Tag.
        :type content: str
        """

        self._content = content

    @property
    def author(self):
        """Gets the author of this Tag.


        :return: The author of this Tag.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Tag.


        :param author: The author of this Tag.
        :type author: str
        """

        self._author = author

    @property
    def authorname(self):
        """Gets the authorname of this Tag.


        :return: The authorname of this Tag.
        :rtype: str
        """
        return self._authorname

    @authorname.setter
    def authorname(self, authorname):
        """Sets the authorname of this Tag.


        :param authorname: The authorname of this Tag.
        :type authorname: str
        """

        self._authorname = authorname

    @property
    def id(self):
        """Gets the id of this Tag.


        :return: The id of this Tag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.


        :param id: The id of this Tag.
        :type id: str
        """

        self._id = id

    @property
    def machine_tag(self):
        """Gets the machine_tag of this Tag.


        :return: The machine_tag of this Tag.
        :rtype: bool
        """
        return self._machine_tag

    @machine_tag.setter
    def machine_tag(self, machine_tag):
        """Sets the machine_tag of this Tag.


        :param machine_tag: The machine_tag of this Tag.
        :type machine_tag: bool
        """

        self._machine_tag = machine_tag

    @property
    def raw(self):
        """Gets the raw of this Tag.


        :return: The raw of this Tag.
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this Tag.


        :param raw: The raw of this Tag.
        :type raw: str
        """

        self._raw = raw
