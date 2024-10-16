# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class StoreNotification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service: str=None, status: str=None, valid_until: int=None):
        """StoreNotification - a model defined in OpenAPI

        :param service: The service of this StoreNotification.
        :param status: The status of this StoreNotification.
        :param valid_until: The valid_until of this StoreNotification.
        """
        self.openapi_types = {
            'service': str,
            'status': str,
            'valid_until': int
        }

        self.attribute_map = {
            'service': 'service',
            'status': 'status',
            'valid_until': 'valid_until'
        }

        self._service = service
        self._status = status
        self._valid_until = valid_until

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StoreNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StoreNotification of this StoreNotification.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service(self):
        """Gets the service of this StoreNotification.


        :return: The service of this StoreNotification.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this StoreNotification.


        :param service: The service of this StoreNotification.
        :type service: str
        """

        self._service = service

    @property
    def status(self):
        """Gets the status of this StoreNotification.


        :return: The status of this StoreNotification.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StoreNotification.


        :param status: The status of this StoreNotification.
        :type status: str
        """

        self._status = status

    @property
    def valid_until(self):
        """Gets the valid_until of this StoreNotification.


        :return: The valid_until of this StoreNotification.
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this StoreNotification.


        :param valid_until: The valid_until of this StoreNotification.
        :type valid_until: int
        """

        self._valid_until = valid_until
