# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, serial: str=None):
        """UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner - a model defined in OpenAPI

        :param serial: The serial of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.
        """
        self.openapi_types = {
            'serial': str
        }

        self.attribute_map = {
            'serial': 'serial'
        }

        self._serial = serial

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateDeviceSensorRelationships_request_livestream_relatedDevices_inner of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def serial(self):
        """Gets the serial of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.

        The serial of the related device

        :return: The serial of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.

        The serial of the related device

        :param serial: The serial of this UpdateDeviceSensorRelationshipsRequestLivestreamRelatedDevicesInner.
        :type serial: str
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")

        self._serial = serial
