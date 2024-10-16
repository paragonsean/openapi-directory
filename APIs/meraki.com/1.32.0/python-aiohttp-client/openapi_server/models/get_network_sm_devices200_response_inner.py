# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSmDevices200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, ip: str=None, name: str=None, notes: str=None, os_name: str=None, serial: str=None, serial_number: str=None, ssid: str=None, system_model: str=None, tags: List[str]=None, uuid: str=None, wifi_mac: str=None):
        """GetNetworkSmDevices200ResponseInner - a model defined in OpenAPI

        :param id: The id of this GetNetworkSmDevices200ResponseInner.
        :param ip: The ip of this GetNetworkSmDevices200ResponseInner.
        :param name: The name of this GetNetworkSmDevices200ResponseInner.
        :param notes: The notes of this GetNetworkSmDevices200ResponseInner.
        :param os_name: The os_name of this GetNetworkSmDevices200ResponseInner.
        :param serial: The serial of this GetNetworkSmDevices200ResponseInner.
        :param serial_number: The serial_number of this GetNetworkSmDevices200ResponseInner.
        :param ssid: The ssid of this GetNetworkSmDevices200ResponseInner.
        :param system_model: The system_model of this GetNetworkSmDevices200ResponseInner.
        :param tags: The tags of this GetNetworkSmDevices200ResponseInner.
        :param uuid: The uuid of this GetNetworkSmDevices200ResponseInner.
        :param wifi_mac: The wifi_mac of this GetNetworkSmDevices200ResponseInner.
        """
        self.openapi_types = {
            'id': str,
            'ip': str,
            'name': str,
            'notes': str,
            'os_name': str,
            'serial': str,
            'serial_number': str,
            'ssid': str,
            'system_model': str,
            'tags': List[str],
            'uuid': str,
            'wifi_mac': str
        }

        self.attribute_map = {
            'id': 'id',
            'ip': 'ip',
            'name': 'name',
            'notes': 'notes',
            'os_name': 'osName',
            'serial': 'serial',
            'serial_number': 'serialNumber',
            'ssid': 'ssid',
            'system_model': 'systemModel',
            'tags': 'tags',
            'uuid': 'uuid',
            'wifi_mac': 'wifiMac'
        }

        self._id = id
        self._ip = ip
        self._name = name
        self._notes = notes
        self._os_name = os_name
        self._serial = serial
        self._serial_number = serial_number
        self._ssid = ssid
        self._system_model = system_model
        self._tags = tags
        self._uuid = uuid
        self._wifi_mac = wifi_mac

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSmDevices200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSmDevices_200_response_inner of this GetNetworkSmDevices200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetNetworkSmDevices200ResponseInner.

        The Meraki Id of the device record.

        :return: The id of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkSmDevices200ResponseInner.

        The Meraki Id of the device record.

        :param id: The id of this GetNetworkSmDevices200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this GetNetworkSmDevices200ResponseInner.

        The IP address of the device.

        :return: The ip of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetNetworkSmDevices200ResponseInner.

        The IP address of the device.

        :param ip: The ip of this GetNetworkSmDevices200ResponseInner.
        :type ip: str
        """

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this GetNetworkSmDevices200ResponseInner.

        The name of the device.

        :return: The name of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetNetworkSmDevices200ResponseInner.

        The name of the device.

        :param name: The name of this GetNetworkSmDevices200ResponseInner.
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this GetNetworkSmDevices200ResponseInner.

        Notes associated with the device.

        :return: The notes of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GetNetworkSmDevices200ResponseInner.

        Notes associated with the device.

        :param notes: The notes of this GetNetworkSmDevices200ResponseInner.
        :type notes: str
        """

        self._notes = notes

    @property
    def os_name(self):
        """Gets the os_name of this GetNetworkSmDevices200ResponseInner.

        The name of the device OS.

        :return: The os_name of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this GetNetworkSmDevices200ResponseInner.

        The name of the device OS.

        :param os_name: The os_name of this GetNetworkSmDevices200ResponseInner.
        :type os_name: str
        """

        self._os_name = os_name

    @property
    def serial(self):
        """Gets the serial of this GetNetworkSmDevices200ResponseInner.

        The device serial.

        :return: The serial of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this GetNetworkSmDevices200ResponseInner.

        The device serial.

        :param serial: The serial of this GetNetworkSmDevices200ResponseInner.
        :type serial: str
        """

        self._serial = serial

    @property
    def serial_number(self):
        """Gets the serial_number of this GetNetworkSmDevices200ResponseInner.

        The device serial number.

        :return: The serial_number of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this GetNetworkSmDevices200ResponseInner.

        The device serial number.

        :param serial_number: The serial_number of this GetNetworkSmDevices200ResponseInner.
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def ssid(self):
        """Gets the ssid of this GetNetworkSmDevices200ResponseInner.

        The name of the SSID the device was last connected to.

        :return: The ssid of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this GetNetworkSmDevices200ResponseInner.

        The name of the SSID the device was last connected to.

        :param ssid: The ssid of this GetNetworkSmDevices200ResponseInner.
        :type ssid: str
        """

        self._ssid = ssid

    @property
    def system_model(self):
        """Gets the system_model of this GetNetworkSmDevices200ResponseInner.

        The device model.

        :return: The system_model of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._system_model

    @system_model.setter
    def system_model(self, system_model):
        """Sets the system_model of this GetNetworkSmDevices200ResponseInner.

        The device model.

        :param system_model: The system_model of this GetNetworkSmDevices200ResponseInner.
        :type system_model: str
        """

        self._system_model = system_model

    @property
    def tags(self):
        """Gets the tags of this GetNetworkSmDevices200ResponseInner.

        An array of tags associated with the device.

        :return: The tags of this GetNetworkSmDevices200ResponseInner.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetNetworkSmDevices200ResponseInner.

        An array of tags associated with the device.

        :param tags: The tags of this GetNetworkSmDevices200ResponseInner.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def uuid(self):
        """Gets the uuid of this GetNetworkSmDevices200ResponseInner.

        The UUID of the device.

        :return: The uuid of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this GetNetworkSmDevices200ResponseInner.

        The UUID of the device.

        :param uuid: The uuid of this GetNetworkSmDevices200ResponseInner.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def wifi_mac(self):
        """Gets the wifi_mac of this GetNetworkSmDevices200ResponseInner.

        The MAC of the device.

        :return: The wifi_mac of this GetNetworkSmDevices200ResponseInner.
        :rtype: str
        """
        return self._wifi_mac

    @wifi_mac.setter
    def wifi_mac(self, wifi_mac):
        """Sets the wifi_mac of this GetNetworkSmDevices200ResponseInner.

        The MAC of the device.

        :param wifi_mac: The wifi_mac of this GetNetworkSmDevices200ResponseInner.
        :type wifi_mac: str
        """

        self._wifi_mac = wifi_mac
