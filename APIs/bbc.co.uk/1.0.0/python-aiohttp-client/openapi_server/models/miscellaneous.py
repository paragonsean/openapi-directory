# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Miscellaneous(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title: str=None):
        """Miscellaneous - a model defined in OpenAPI

        :param title: The title of this Miscellaneous.
        """
        self.openapi_types = {
            'title': str
        }

        self.attribute_map = {
            'title': 'title'
        }

        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Miscellaneous':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Miscellaneous of this Miscellaneous.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this Miscellaneous.


        :return: The title of this Miscellaneous.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Miscellaneous.


        :param title: The title of this Miscellaneous.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title
