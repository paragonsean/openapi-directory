# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WarningItemsWarningInnerWarningInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text: str=None, short_description: str=None, warning_code: str=None):
        """WarningItemsWarningInnerWarningInner - a model defined in OpenAPI

        :param text: The text of this WarningItemsWarningInnerWarningInner.
        :param short_description: The short_description of this WarningItemsWarningInnerWarningInner.
        :param warning_code: The warning_code of this WarningItemsWarningInnerWarningInner.
        """
        self.openapi_types = {
            'text': str,
            'short_description': str,
            'warning_code': str
        }

        self.attribute_map = {
            'text': '#text',
            'short_description': 'short_description',
            'warning_code': 'warning_code'
        }

        self._text = text
        self._short_description = short_description
        self._warning_code = warning_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WarningItemsWarningInnerWarningInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The warning_items_warning_inner_warning_inner of this WarningItemsWarningInnerWarningInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this WarningItemsWarningInnerWarningInner.


        :return: The text of this WarningItemsWarningInnerWarningInner.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WarningItemsWarningInnerWarningInner.


        :param text: The text of this WarningItemsWarningInnerWarningInner.
        :type text: str
        """

        self._text = text

    @property
    def short_description(self):
        """Gets the short_description of this WarningItemsWarningInnerWarningInner.


        :return: The short_description of this WarningItemsWarningInnerWarningInner.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this WarningItemsWarningInnerWarningInner.


        :param short_description: The short_description of this WarningItemsWarningInnerWarningInner.
        :type short_description: str
        """

        self._short_description = short_description

    @property
    def warning_code(self):
        """Gets the warning_code of this WarningItemsWarningInnerWarningInner.


        :return: The warning_code of this WarningItemsWarningInnerWarningInner.
        :rtype: str
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, warning_code):
        """Sets the warning_code of this WarningItemsWarningInnerWarningInner.


        :param warning_code: The warning_code of this WarningItemsWarningInnerWarningInner.
        :type warning_code: str
        """

        self._warning_code = warning_code
