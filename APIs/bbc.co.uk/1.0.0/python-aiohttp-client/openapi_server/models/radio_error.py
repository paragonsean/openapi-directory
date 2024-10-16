# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RadioError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, detail: str=None, href: str=None, id: str=None, status: int=None, timestamp: int=None, title: str=None):
        """RadioError - a model defined in OpenAPI

        :param code: The code of this RadioError.
        :param detail: The detail of this RadioError.
        :param href: The href of this RadioError.
        :param id: The id of this RadioError.
        :param status: The status of this RadioError.
        :param timestamp: The timestamp of this RadioError.
        :param title: The title of this RadioError.
        """
        self.openapi_types = {
            'code': str,
            'detail': str,
            'href': str,
            'id': str,
            'status': int,
            'timestamp': int,
            'title': str
        }

        self.attribute_map = {
            'code': 'code',
            'detail': 'detail',
            'href': 'href',
            'id': 'id',
            'status': 'status',
            'timestamp': 'timestamp',
            'title': 'title'
        }

        self._code = code
        self._detail = detail
        self._href = href
        self._id = id
        self._status = status
        self._timestamp = timestamp
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RadioError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RadioError of this RadioError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this RadioError.


        :return: The code of this RadioError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RadioError.


        :param code: The code of this RadioError.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this RadioError.


        :return: The detail of this RadioError.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RadioError.


        :param detail: The detail of this RadioError.
        :type detail: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")

        self._detail = detail

    @property
    def href(self):
        """Gets the href of this RadioError.


        :return: The href of this RadioError.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this RadioError.


        :param href: The href of this RadioError.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def id(self):
        """Gets the id of this RadioError.


        :return: The id of this RadioError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RadioError.


        :param id: The id of this RadioError.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def status(self):
        """Gets the status of this RadioError.


        :return: The status of this RadioError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RadioError.


        :param status: The status of this RadioError.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def timestamp(self):
        """Gets the timestamp of this RadioError.


        :return: The timestamp of this RadioError.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RadioError.


        :param timestamp: The timestamp of this RadioError.
        :type timestamp: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def title(self):
        """Gets the title of this RadioError.


        :return: The title of this RadioError.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RadioError.


        :param title: The title of this RadioError.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title
