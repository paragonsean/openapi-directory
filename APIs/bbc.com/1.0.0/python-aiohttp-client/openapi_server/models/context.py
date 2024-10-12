# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class Context(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cascades_to_descendants: bool=None, href: str=None, pid: str=None, result_type: str=None):
        """Context - a model defined in OpenAPI

        :param cascades_to_descendants: The cascades_to_descendants of this Context.
        :param href: The href of this Context.
        :param pid: The pid of this Context.
        :param result_type: The result_type of this Context.
        """
        self.openapi_types = {
            'cascades_to_descendants': bool,
            'href': str,
            'pid': str,
            'result_type': str
        }

        self.attribute_map = {
            'cascades_to_descendants': 'cascades_to_descendants',
            'href': 'href',
            'pid': 'pid',
            'result_type': 'result_type'
        }

        self._cascades_to_descendants = cascades_to_descendants
        self._href = href
        self._pid = pid
        self._result_type = result_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Context':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The context of this Context.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cascades_to_descendants(self):
        """Gets the cascades_to_descendants of this Context.


        :return: The cascades_to_descendants of this Context.
        :rtype: bool
        """
        return self._cascades_to_descendants

    @cascades_to_descendants.setter
    def cascades_to_descendants(self, cascades_to_descendants):
        """Sets the cascades_to_descendants of this Context.


        :param cascades_to_descendants: The cascades_to_descendants of this Context.
        :type cascades_to_descendants: bool
        """

        self._cascades_to_descendants = cascades_to_descendants

    @property
    def href(self):
        """Gets the href of this Context.


        :return: The href of this Context.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Context.


        :param href: The href of this Context.
        :type href: str
        """

        self._href = href

    @property
    def pid(self):
        """Gets the pid of this Context.


        :return: The pid of this Context.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this Context.


        :param pid: The pid of this Context.
        :type pid: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")
        if pid is not None and not re.search(r'([a-z0-9\.\-]+|.*PID.*)', pid):
            raise ValueError("Invalid value for `pid`, must be a follow pattern or equal to `/([a-z0-9\.\-]+|.*PID.*)/`")

        self._pid = pid

    @property
    def result_type(self):
        """Gets the result_type of this Context.


        :return: The result_type of this Context.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this Context.


        :param result_type: The result_type of this Context.
        :type result_type: str
        """
        if result_type is None:
            raise ValueError("Invalid value for `result_type`, must not be `None`")

        self._result_type = result_type
