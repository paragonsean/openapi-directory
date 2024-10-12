# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.fetchrequest import Fetchrequest
from openapi_server.models.model_field import ModelField
from openapi_server.models.paginator import Paginator
from openapi_server import util


class Parserequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, common_parent: str=None, fields: List[ModelField]=None, format: str=None, name: str=None, paginator: Paginator=None, path: bool=False, request: Fetchrequest=None):
        """Parserequest - a model defined in OpenAPI

        :param common_parent: The common_parent of this Parserequest.
        :param fields: The fields of this Parserequest.
        :param format: The format of this Parserequest.
        :param name: The name of this Parserequest.
        :param paginator: The paginator of this Parserequest.
        :param path: The path of this Parserequest.
        :param request: The request of this Parserequest.
        """
        self.openapi_types = {
            'common_parent': str,
            'fields': List[ModelField],
            'format': str,
            'name': str,
            'paginator': Paginator,
            'path': bool,
            'request': Fetchrequest
        }

        self.attribute_map = {
            'common_parent': 'commonParent',
            'fields': 'fields',
            'format': 'format',
            'name': 'name',
            'paginator': 'paginator',
            'path': 'path',
            'request': 'request'
        }

        self._common_parent = common_parent
        self._fields = fields
        self._format = format
        self._name = name
        self._paginator = paginator
        self._path = path
        self._request = request

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Parserequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The parserequest of this Parserequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def common_parent(self):
        """Gets the common_parent of this Parserequest.

        Specifies common ancestor block for a set of fields used to extract data from a web page. _(CSS Selector)_

        :return: The common_parent of this Parserequest.
        :rtype: str
        """
        return self._common_parent

    @common_parent.setter
    def common_parent(self, common_parent):
        """Sets the common_parent of this Parserequest.

        Specifies common ancestor block for a set of fields used to extract data from a web page. _(CSS Selector)_

        :param common_parent: The common_parent of this Parserequest.
        :type common_parent: str
        """

        self._common_parent = common_parent

    @property
    def fields(self):
        """Gets the fields of this Parserequest.

        Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page. 

        :return: The fields of this Parserequest.
        :rtype: List[ModelField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Parserequest.

        Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page. 

        :param fields: The fields of this Parserequest.
        :type fields: List[ModelField]
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")

        self._fields = fields

    @property
    def format(self):
        """Gets the format of this Parserequest.

        Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.

        :return: The format of this Parserequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Parserequest.

        Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.

        :param format: The format of this Parserequest.
        :type format: str
        """
        allowed_values = ["csv", "json", "jsonl", "excel", "xml"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def name(self):
        """Gets the name of this Parserequest.

        Collection name.

        :return: The name of this Parserequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parserequest.

        Collection name.

        :param name: The name of this Parserequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def paginator(self):
        """Gets the paginator of this Parserequest.


        :return: The paginator of this Parserequest.
        :rtype: Paginator
        """
        return self._paginator

    @paginator.setter
    def paginator(self, paginator):
        """Sets the paginator of this Parserequest.


        :param paginator: The paginator of this Parserequest.
        :type paginator: Paginator
        """

        self._paginator = paginator

    @property
    def path(self):
        """Gets the path of this Parserequest.

        Path is a special parameter specifying navigation pages only. It collects information from detailed pages. No results from the current page return. Defaults to false.

        :return: The path of this Parserequest.
        :rtype: bool
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Parserequest.

        Path is a special parameter specifying navigation pages only. It collects information from detailed pages. No results from the current page return. Defaults to false.

        :param path: The path of this Parserequest.
        :type path: bool
        """

        self._path = path

    @property
    def request(self):
        """Gets the request of this Parserequest.


        :return: The request of this Parserequest.
        :rtype: Fetchrequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Parserequest.


        :param request: The request of this Parserequest.
        :type request: Fetchrequest
        """

        self._request = request
