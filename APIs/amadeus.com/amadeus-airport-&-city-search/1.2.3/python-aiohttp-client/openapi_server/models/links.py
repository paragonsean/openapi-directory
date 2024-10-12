# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Links(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, href: str=None, methods: List[str]=None):
        """Links - a model defined in OpenAPI

        :param count: The count of this Links.
        :param href: The href of this Links.
        :param methods: The methods of this Links.
        """
        self.openapi_types = {
            'count': int,
            'href': str,
            'methods': List[str]
        }

        self.attribute_map = {
            'count': 'count',
            'href': 'href',
            'methods': 'methods'
        }

        self._count = count
        self._href = href
        self._methods = methods

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Links':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Links of this Links.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this Links.


        :return: The count of this Links.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Links.


        :param count: The count of this Links.
        :type count: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this Links.


        :return: The href of this Links.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Links.


        :param href: The href of this Links.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def methods(self):
        """Gets the methods of this Links.


        :return: The methods of this Links.
        :rtype: List[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this Links.


        :param methods: The methods of this Links.
        :type methods: List[str]
        """
        allowed_values = ["GET", "PUT", "DELETE", "POST", "PATCH"]  # noqa: E501
        if not set(methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `methods` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(methods) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._methods = methods
