# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.task_section_group import TaskSectionGroup
from openapi_server import util


class TaskDropdownList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, page_size: int=None, has_more: bool=None, page_number: int=None, sections: List[TaskSectionGroup]=None):
        """TaskDropdownList - a model defined in OpenAPI

        :param page_size: The page_size of this TaskDropdownList.
        :param has_more: The has_more of this TaskDropdownList.
        :param page_number: The page_number of this TaskDropdownList.
        :param sections: The sections of this TaskDropdownList.
        """
        self.openapi_types = {
            'page_size': int,
            'has_more': bool,
            'page_number': int,
            'sections': List[TaskSectionGroup]
        }

        self.attribute_map = {
            'page_size': 'PageSize',
            'has_more': 'hasMore',
            'page_number': 'pageNumber',
            'sections': 'sections'
        }

        self._page_size = page_size
        self._has_more = has_more
        self._page_number = page_number
        self._sections = sections

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaskDropdownList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaskDropdownList of this TaskDropdownList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def page_size(self):
        """Gets the page_size of this TaskDropdownList.

        Current page size

        :return: The page_size of this TaskDropdownList.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TaskDropdownList.

        Current page size

        :param page_size: The page_size of this TaskDropdownList.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def has_more(self):
        """Gets the has_more of this TaskDropdownList.

        More records probably exist

        :return: The has_more of this TaskDropdownList.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this TaskDropdownList.

        More records probably exist

        :param has_more: The has_more of this TaskDropdownList.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def page_number(self):
        """Gets the page_number of this TaskDropdownList.

        Current page number (1 based)

        :return: The page_number of this TaskDropdownList.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this TaskDropdownList.

        Current page number (1 based)

        :param page_number: The page_number of this TaskDropdownList.
        :type page_number: int
        """

        self._page_number = page_number

    @property
    def sections(self):
        """Gets the sections of this TaskDropdownList.

        List of Task grouped by Section

        :return: The sections of this TaskDropdownList.
        :rtype: List[TaskSectionGroup]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this TaskDropdownList.

        List of Task grouped by Section

        :param sections: The sections of this TaskDropdownList.
        :type sections: List[TaskSectionGroup]
        """

        self._sections = sections
