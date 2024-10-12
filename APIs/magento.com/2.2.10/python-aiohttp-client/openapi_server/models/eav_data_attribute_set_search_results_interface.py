# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.eav_data_attribute_set_interface import EavDataAttributeSetInterface
from openapi_server.models.framework_search_criteria_interface import FrameworkSearchCriteriaInterface
from openapi_server import util


class EavDataAttributeSetSearchResultsInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[EavDataAttributeSetInterface]=None, search_criteria: FrameworkSearchCriteriaInterface=None, total_count: int=None):
        """EavDataAttributeSetSearchResultsInterface - a model defined in OpenAPI

        :param items: The items of this EavDataAttributeSetSearchResultsInterface.
        :param search_criteria: The search_criteria of this EavDataAttributeSetSearchResultsInterface.
        :param total_count: The total_count of this EavDataAttributeSetSearchResultsInterface.
        """
        self.openapi_types = {
            'items': List[EavDataAttributeSetInterface],
            'search_criteria': FrameworkSearchCriteriaInterface,
            'total_count': int
        }

        self.attribute_map = {
            'items': 'items',
            'search_criteria': 'search_criteria',
            'total_count': 'total_count'
        }

        self._items = items
        self._search_criteria = search_criteria
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EavDataAttributeSetSearchResultsInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The eav-data-attribute-set-search-results-interface of this EavDataAttributeSetSearchResultsInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this EavDataAttributeSetSearchResultsInterface.

        Attribute sets list.

        :return: The items of this EavDataAttributeSetSearchResultsInterface.
        :rtype: List[EavDataAttributeSetInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this EavDataAttributeSetSearchResultsInterface.

        Attribute sets list.

        :param items: The items of this EavDataAttributeSetSearchResultsInterface.
        :type items: List[EavDataAttributeSetInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def search_criteria(self):
        """Gets the search_criteria of this EavDataAttributeSetSearchResultsInterface.


        :return: The search_criteria of this EavDataAttributeSetSearchResultsInterface.
        :rtype: FrameworkSearchCriteriaInterface
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this EavDataAttributeSetSearchResultsInterface.


        :param search_criteria: The search_criteria of this EavDataAttributeSetSearchResultsInterface.
        :type search_criteria: FrameworkSearchCriteriaInterface
        """
        if search_criteria is None:
            raise ValueError("Invalid value for `search_criteria`, must not be `None`")

        self._search_criteria = search_criteria

    @property
    def total_count(self):
        """Gets the total_count of this EavDataAttributeSetSearchResultsInterface.

        Total count.

        :return: The total_count of this EavDataAttributeSetSearchResultsInterface.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this EavDataAttributeSetSearchResultsInterface.

        Total count.

        :param total_count: The total_count of this EavDataAttributeSetSearchResultsInterface.
        :type total_count: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count
