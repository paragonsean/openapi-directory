# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class CalendarEventResponseResourceLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _self: str=None):
        """CalendarEventResponseResourceLinks - a model defined in OpenAPI

        :param _self: The _self of this CalendarEventResponseResourceLinks.
        """
        self.openapi_types = {
            '_self': str
        }

        self.attribute_map = {
            '_self': 'self'
        }

        self.__self = _self

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CalendarEventResponseResourceLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CalendarEventResponseResource_links of this CalendarEventResponseResourceLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self):
        """Gets the _self of this CalendarEventResponseResourceLinks.


        :return: The _self of this CalendarEventResponseResourceLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CalendarEventResponseResourceLinks.


        :param _self: The _self of this CalendarEventResponseResourceLinks.
        :type _self: str
        """
        if _self is not None and not re.search(r'calendar_event_response', _self):
            raise ValueError("Invalid value for `_self`, must be a follow pattern or equal to `/calendar_event_response/[0-9a-z]+`")

        self.__self = _self
