# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProblemDetail(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, detail: str=None, status: int=None, title: str=None, type: str=None):
        """ProblemDetail - a model defined in OpenAPI

        :param detail: The detail of this ProblemDetail.
        :param status: The status of this ProblemDetail.
        :param title: The title of this ProblemDetail.
        :param type: The type of this ProblemDetail.
        """
        self.openapi_types = {
            'detail': str,
            'status': int,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'status': 'status',
            'title': 'title',
            'type': 'type'
        }

        self._detail = detail
        self._status = status
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProblemDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The problem_detail of this ProblemDetail.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self):
        """Gets the detail of this ProblemDetail.


        :return: The detail of this ProblemDetail.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetail.


        :param detail: The detail of this ProblemDetail.
        :type detail: str
        """

        self._detail = detail

    @property
    def status(self):
        """Gets the status of this ProblemDetail.


        :return: The status of this ProblemDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetail.


        :param status: The status of this ProblemDetail.
        :type status: int
        """

        self._status = status

    @property
    def title(self):
        """Gets the title of this ProblemDetail.


        :return: The title of this ProblemDetail.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetail.


        :param title: The title of this ProblemDetail.
        :type title: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this ProblemDetail.


        :return: The type of this ProblemDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetail.


        :param type: The type of this ProblemDetail.
        :type type: str
        """

        self._type = type
