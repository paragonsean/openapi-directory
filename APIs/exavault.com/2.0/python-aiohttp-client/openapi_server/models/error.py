# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Error(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, detail: str=None, meta: object=None, title: str=None):
        """Error - a model defined in OpenAPI

        :param code: The code of this Error.
        :param detail: The detail of this Error.
        :param meta: The meta of this Error.
        :param title: The title of this Error.
        """
        self.openapi_types = {
            'code': str,
            'detail': str,
            'meta': object,
            'title': str
        }

        self.attribute_map = {
            'code': 'code',
            'detail': 'detail',
            'meta': 'meta',
            'title': 'title'
        }

        self._code = code
        self._detail = detail
        self._meta = meta
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error of this Error.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Error.

        Specific internal error string.

        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        Specific internal error string.

        :param code: The code of this Error.
        :type code: str
        """

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error.

        human-readable explanation specific to this occurrence of the problem.

        :return: The detail of this Error.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        human-readable explanation specific to this occurrence of the problem.

        :param detail: The detail of this Error.
        :type detail: str
        """

        self._detail = detail

    @property
    def meta(self):
        """Gets the meta of this Error.

        Meta object containing non-standard meta-information about the error.

        :return: The meta of this Error.
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Error.

        Meta object containing non-standard meta-information about the error.

        :param meta: The meta of this Error.
        :type meta: object
        """

        self._meta = meta

    @property
    def title(self):
        """Gets the title of this Error.

        Human readable summary of the problem.

        :return: The title of this Error.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error.

        Human readable summary of the problem.

        :param title: The title of this Error.
        :type title: str
        """

        self._title = title
