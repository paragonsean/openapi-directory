# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.yara_meta import YaraMeta
from openapi_server import util


class Yara(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meta: YaraMeta=None, name: str=None, strings: List[List[str]]=None):
        """Yara - a model defined in OpenAPI

        :param meta: The meta of this Yara.
        :param name: The name of this Yara.
        :param strings: The strings of this Yara.
        """
        self.openapi_types = {
            'meta': YaraMeta,
            'name': str,
            'strings': List[List[str]]
        }

        self.attribute_map = {
            'meta': 'meta',
            'name': 'name',
            'strings': 'strings'
        }

        self._meta = meta
        self._name = name
        self._strings = strings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Yara':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The yara of this Yara.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self):
        """Gets the meta of this Yara.


        :return: The meta of this Yara.
        :rtype: YaraMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Yara.


        :param meta: The meta of this Yara.
        :type meta: YaraMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Yara.

        Yara rule name

        :return: The name of this Yara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Yara.

        Yara rule name

        :param name: The name of this Yara.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def strings(self):
        """Gets the strings of this Yara.

        Yara rule string section

        :return: The strings of this Yara.
        :rtype: List[List[str]]
        """
        return self._strings

    @strings.setter
    def strings(self, strings):
        """Sets the strings of this Yara.

        Yara rule string section

        :param strings: The strings of this Yara.
        :type strings: List[List[str]]
        """
        if strings is None:
            raise ValueError("Invalid value for `strings`, must not be `None`")

        self._strings = strings
