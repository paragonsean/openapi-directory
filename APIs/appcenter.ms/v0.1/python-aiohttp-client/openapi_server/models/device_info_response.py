# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DeviceInfoResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_name: str=None, full_device_name: str=None, imei: str=None, model: str=None, os_build: str=None, os_version: str=None, owner_id: str=None, registered_at: str=None, serial: str=None, status: str=None, udid: str=None):
        """DeviceInfoResponse - a model defined in OpenAPI

        :param device_name: The device_name of this DeviceInfoResponse.
        :param full_device_name: The full_device_name of this DeviceInfoResponse.
        :param imei: The imei of this DeviceInfoResponse.
        :param model: The model of this DeviceInfoResponse.
        :param os_build: The os_build of this DeviceInfoResponse.
        :param os_version: The os_version of this DeviceInfoResponse.
        :param owner_id: The owner_id of this DeviceInfoResponse.
        :param registered_at: The registered_at of this DeviceInfoResponse.
        :param serial: The serial of this DeviceInfoResponse.
        :param status: The status of this DeviceInfoResponse.
        :param udid: The udid of this DeviceInfoResponse.
        """
        self.openapi_types = {
            'device_name': str,
            'full_device_name': str,
            'imei': str,
            'model': str,
            'os_build': str,
            'os_version': str,
            'owner_id': str,
            'registered_at': str,
            'serial': str,
            'status': str,
            'udid': str
        }

        self.attribute_map = {
            'device_name': 'device_name',
            'full_device_name': 'full_device_name',
            'imei': 'imei',
            'model': 'model',
            'os_build': 'os_build',
            'os_version': 'os_version',
            'owner_id': 'owner_id',
            'registered_at': 'registered_at',
            'serial': 'serial',
            'status': 'status',
            'udid': 'udid'
        }

        self._device_name = device_name
        self._full_device_name = full_device_name
        self._imei = imei
        self._model = model
        self._os_build = os_build
        self._os_version = os_version
        self._owner_id = owner_id
        self._registered_at = registered_at
        self._serial = serial
        self._status = status
        self._udid = udid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeviceInfoResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeviceInfoResponse of this DeviceInfoResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_name(self):
        """Gets the device_name of this DeviceInfoResponse.

        The device description, in the format \"iPhone 7 Plus (A1784)\"

        :return: The device_name of this DeviceInfoResponse.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DeviceInfoResponse.

        The device description, in the format \"iPhone 7 Plus (A1784)\"

        :param device_name: The device_name of this DeviceInfoResponse.
        :type device_name: str
        """
        if device_name is None:
            raise ValueError("Invalid value for `device_name`, must not be `None`")

        self._device_name = device_name

    @property
    def full_device_name(self):
        """Gets the full_device_name of this DeviceInfoResponse.

        A combination of the device model name and the owner name.

        :return: The full_device_name of this DeviceInfoResponse.
        :rtype: str
        """
        return self._full_device_name

    @full_device_name.setter
    def full_device_name(self, full_device_name):
        """Sets the full_device_name of this DeviceInfoResponse.

        A combination of the device model name and the owner name.

        :param full_device_name: The full_device_name of this DeviceInfoResponse.
        :type full_device_name: str
        """

        self._full_device_name = full_device_name

    @property
    def imei(self):
        """Gets the imei of this DeviceInfoResponse.

        The device's International Mobile Equipment Identity number. Always empty or undefined at present.

        :return: The imei of this DeviceInfoResponse.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this DeviceInfoResponse.

        The device's International Mobile Equipment Identity number. Always empty or undefined at present.

        :param imei: The imei of this DeviceInfoResponse.
        :type imei: str
        """

        self._imei = imei

    @property
    def model(self):
        """Gets the model of this DeviceInfoResponse.

        The model identifier of the device, in the format iDeviceM,N

        :return: The model of this DeviceInfoResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceInfoResponse.

        The model identifier of the device, in the format iDeviceM,N

        :param model: The model of this DeviceInfoResponse.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")

        self._model = model

    @property
    def os_build(self):
        """Gets the os_build of this DeviceInfoResponse.

        The last known OS version running on the device

        :return: The os_build of this DeviceInfoResponse.
        :rtype: str
        """
        return self._os_build

    @os_build.setter
    def os_build(self, os_build):
        """Sets the os_build of this DeviceInfoResponse.

        The last known OS version running on the device

        :param os_build: The os_build of this DeviceInfoResponse.
        :type os_build: str
        """
        if os_build is None:
            raise ValueError("Invalid value for `os_build`, must not be `None`")

        self._os_build = os_build

    @property
    def os_version(self):
        """Gets the os_version of this DeviceInfoResponse.

        The last known OS version running on the device

        :return: The os_version of this DeviceInfoResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this DeviceInfoResponse.

        The last known OS version running on the device

        :param os_version: The os_version of this DeviceInfoResponse.
        :type os_version: str
        """
        if os_version is None:
            raise ValueError("Invalid value for `os_version`, must not be `None`")

        self._os_version = os_version

    @property
    def owner_id(self):
        """Gets the owner_id of this DeviceInfoResponse.

        The user ID of the device owner.

        :return: The owner_id of this DeviceInfoResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DeviceInfoResponse.

        The user ID of the device owner.

        :param owner_id: The owner_id of this DeviceInfoResponse.
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def registered_at(self):
        """Gets the registered_at of this DeviceInfoResponse.

        Timestamp of when the device was registered in ISO format.

        :return: The registered_at of this DeviceInfoResponse.
        :rtype: str
        """
        return self._registered_at

    @registered_at.setter
    def registered_at(self, registered_at):
        """Sets the registered_at of this DeviceInfoResponse.

        Timestamp of when the device was registered in ISO format.

        :param registered_at: The registered_at of this DeviceInfoResponse.
        :type registered_at: str
        """

        self._registered_at = registered_at

    @property
    def serial(self):
        """Gets the serial of this DeviceInfoResponse.

        The device's serial number. Always empty or undefined at present.

        :return: The serial of this DeviceInfoResponse.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeviceInfoResponse.

        The device's serial number. Always empty or undefined at present.

        :param serial: The serial of this DeviceInfoResponse.
        :type serial: str
        """

        self._serial = serial

    @property
    def status(self):
        """Gets the status of this DeviceInfoResponse.

        The provisioning status of the device.

        :return: The status of this DeviceInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceInfoResponse.

        The provisioning status of the device.

        :param status: The status of this DeviceInfoResponse.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def udid(self):
        """Gets the udid of this DeviceInfoResponse.

        The Unique Device IDentifier of the device

        :return: The udid of this DeviceInfoResponse.
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this DeviceInfoResponse.

        The Unique Device IDentifier of the device

        :param udid: The udid of this DeviceInfoResponse.
        :type udid: str
        """
        if udid is None:
            raise ValueError("Invalid value for `udid`, must not be `None`")

        self._udid = udid
