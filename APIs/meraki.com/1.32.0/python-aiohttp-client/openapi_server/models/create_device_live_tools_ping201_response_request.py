# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateDeviceLiveToolsPing201ResponseRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, serial: str=None, target: str=None):
        """CreateDeviceLiveToolsPing201ResponseRequest - a model defined in OpenAPI

        :param count: The count of this CreateDeviceLiveToolsPing201ResponseRequest.
        :param serial: The serial of this CreateDeviceLiveToolsPing201ResponseRequest.
        :param target: The target of this CreateDeviceLiveToolsPing201ResponseRequest.
        """
        self.openapi_types = {
            'count': int,
            'serial': str,
            'target': str
        }

        self.attribute_map = {
            'count': 'count',
            'serial': 'serial',
            'target': 'target'
        }

        self._count = count
        self._serial = serial
        self._target = target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateDeviceLiveToolsPing201ResponseRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createDeviceLiveToolsPing_201_response_request of this CreateDeviceLiveToolsPing201ResponseRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this CreateDeviceLiveToolsPing201ResponseRequest.

        Number of pings to send

        :return: The count of this CreateDeviceLiveToolsPing201ResponseRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateDeviceLiveToolsPing201ResponseRequest.

        Number of pings to send

        :param count: The count of this CreateDeviceLiveToolsPing201ResponseRequest.
        :type count: int
        """

        self._count = count

    @property
    def serial(self):
        """Gets the serial of this CreateDeviceLiveToolsPing201ResponseRequest.

        Device serial number

        :return: The serial of this CreateDeviceLiveToolsPing201ResponseRequest.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this CreateDeviceLiveToolsPing201ResponseRequest.

        Device serial number

        :param serial: The serial of this CreateDeviceLiveToolsPing201ResponseRequest.
        :type serial: str
        """

        self._serial = serial

    @property
    def target(self):
        """Gets the target of this CreateDeviceLiveToolsPing201ResponseRequest.

        IP address or FQDN to ping

        :return: The target of this CreateDeviceLiveToolsPing201ResponseRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CreateDeviceLiveToolsPing201ResponseRequest.

        IP address or FQDN to ping

        :param target: The target of this CreateDeviceLiveToolsPing201ResponseRequest.
        :type target: str
        """

        self._target = target
