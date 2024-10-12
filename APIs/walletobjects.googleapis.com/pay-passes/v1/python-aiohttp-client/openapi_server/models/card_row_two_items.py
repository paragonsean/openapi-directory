# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.template_item import TemplateItem
from openapi_server import util


class CardRowTwoItems(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_item: TemplateItem=None, start_item: TemplateItem=None):
        """CardRowTwoItems - a model defined in OpenAPI

        :param end_item: The end_item of this CardRowTwoItems.
        :param start_item: The start_item of this CardRowTwoItems.
        """
        self.openapi_types = {
            'end_item': TemplateItem,
            'start_item': TemplateItem
        }

        self.attribute_map = {
            'end_item': 'endItem',
            'start_item': 'startItem'
        }

        self._end_item = end_item
        self._start_item = start_item

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CardRowTwoItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CardRowTwoItems of this CardRowTwoItems.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_item(self):
        """Gets the end_item of this CardRowTwoItems.


        :return: The end_item of this CardRowTwoItems.
        :rtype: TemplateItem
        """
        return self._end_item

    @end_item.setter
    def end_item(self, end_item):
        """Sets the end_item of this CardRowTwoItems.


        :param end_item: The end_item of this CardRowTwoItems.
        :type end_item: TemplateItem
        """

        self._end_item = end_item

    @property
    def start_item(self):
        """Gets the start_item of this CardRowTwoItems.


        :return: The start_item of this CardRowTwoItems.
        :rtype: TemplateItem
        """
        return self._start_item

    @start_item.setter
    def start_item(self, start_item):
        """Sets the start_item of this CardRowTwoItems.


        :param start_item: The start_item of this CardRowTwoItems.
        :type start_item: TemplateItem
        """

        self._start_item = start_item
