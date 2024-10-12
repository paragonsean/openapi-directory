# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.metadatum import Metadatum
from openapi_server import util


class HTTPHealthCheck(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host: str=None, path: str=None, request_headers_to_add: List[Metadatum]=None, service_name: str=None):
        """HTTPHealthCheck - a model defined in OpenAPI

        :param host: The host of this HTTPHealthCheck.
        :param path: The path of this HTTPHealthCheck.
        :param request_headers_to_add: The request_headers_to_add of this HTTPHealthCheck.
        :param service_name: The service_name of this HTTPHealthCheck.
        """
        self.openapi_types = {
            'host': str,
            'path': str,
            'request_headers_to_add': List[Metadatum],
            'service_name': str
        }

        self.attribute_map = {
            'host': 'host',
            'path': 'path',
            'request_headers_to_add': 'request_headers_to_add',
            'service_name': 'service_name'
        }

        self._host = host
        self._path = path
        self._request_headers_to_add = request_headers_to_add
        self._service_name = service_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HTTPHealthCheck':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HTTPHealthCheck of this HTTPHealthCheck.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self):
        """Gets the host of this HTTPHealthCheck.

        The value of the host header in the HTTP health check request. If left empty, the name of the cluster being health checked will be used. 

        :return: The host of this HTTPHealthCheck.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HTTPHealthCheck.

        The value of the host header in the HTTP health check request. If left empty, the name of the cluster being health checked will be used. 

        :param host: The host of this HTTPHealthCheck.
        :type host: str
        """

        self._host = host

    @property
    def path(self):
        """Gets the path of this HTTPHealthCheck.

        Specifies the HTTP path that will be requested during health checking. 

        :return: The path of this HTTPHealthCheck.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HTTPHealthCheck.

        Specifies the HTTP path that will be requested during health checking. 

        :param path: The path of this HTTPHealthCheck.
        :type path: str
        """

        self._path = path

    @property
    def request_headers_to_add(self):
        """Gets the request_headers_to_add of this HTTPHealthCheck.

        Specifies a list of HTTP headers that should be added to each request sent to the health checked cluster. 

        :return: The request_headers_to_add of this HTTPHealthCheck.
        :rtype: List[Metadatum]
        """
        return self._request_headers_to_add

    @request_headers_to_add.setter
    def request_headers_to_add(self, request_headers_to_add):
        """Sets the request_headers_to_add of this HTTPHealthCheck.

        Specifies a list of HTTP headers that should be added to each request sent to the health checked cluster. 

        :param request_headers_to_add: The request_headers_to_add of this HTTPHealthCheck.
        :type request_headers_to_add: List[Metadatum]
        """

        self._request_headers_to_add = request_headers_to_add

    @property
    def service_name(self):
        """Gets the service_name of this HTTPHealthCheck.

        An optional service name parameter which is used to validate the identity of the health checked cluster. 

        :return: The service_name of this HTTPHealthCheck.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this HTTPHealthCheck.

        An optional service name parameter which is used to validate the identity of the health checked cluster. 

        :param service_name: The service_name of this HTTPHealthCheck.
        :type service_name: str
        """

        self._service_name = service_name
