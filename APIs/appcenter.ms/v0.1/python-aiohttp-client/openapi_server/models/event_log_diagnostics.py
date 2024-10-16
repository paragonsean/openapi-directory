# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EventLogDiagnostics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, session_id: str=None, properties: Dict[str, str]=None, device: object=None, install_id: str=None, timestamp: datetime=None, type: str=None):
        """EventLogDiagnostics - a model defined in OpenAPI

        :param id: The id of this EventLogDiagnostics.
        :param name: The name of this EventLogDiagnostics.
        :param session_id: The session_id of this EventLogDiagnostics.
        :param properties: The properties of this EventLogDiagnostics.
        :param device: The device of this EventLogDiagnostics.
        :param install_id: The install_id of this EventLogDiagnostics.
        :param timestamp: The timestamp of this EventLogDiagnostics.
        :param type: The type of this EventLogDiagnostics.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'session_id': str,
            'properties': Dict[str, str],
            'device': object,
            'install_id': str,
            'timestamp': datetime,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'session_id': 'session_id',
            'properties': 'properties',
            'device': 'device',
            'install_id': 'install_id',
            'timestamp': 'timestamp',
            'type': 'type'
        }

        self._id = id
        self._name = name
        self._session_id = session_id
        self._properties = properties
        self._device = device
        self._install_id = install_id
        self._timestamp = timestamp
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EventLogDiagnostics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EventLog_Diagnostics of this EventLogDiagnostics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EventLogDiagnostics.

        Unique identifier for this event. 

        :return: The id of this EventLogDiagnostics.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventLogDiagnostics.

        Unique identifier for this event. 

        :param id: The id of this EventLogDiagnostics.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this EventLogDiagnostics.

        Name of the event. 

        :return: The name of this EventLogDiagnostics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventLogDiagnostics.

        Name of the event. 

        :param name: The name of this EventLogDiagnostics.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def session_id(self):
        """Gets the session_id of this EventLogDiagnostics.

        Session ID. 

        :return: The session_id of this EventLogDiagnostics.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this EventLogDiagnostics.

        Session ID. 

        :param session_id: The session_id of this EventLogDiagnostics.
        :type session_id: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")

        self._session_id = session_id

    @property
    def properties(self):
        """Gets the properties of this EventLogDiagnostics.

        Additional key/value pair parameters. 

        :return: The properties of this EventLogDiagnostics.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EventLogDiagnostics.

        Additional key/value pair parameters. 

        :param properties: The properties of this EventLogDiagnostics.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def device(self):
        """Gets the device of this EventLogDiagnostics.

        Device characteristics.

        :return: The device of this EventLogDiagnostics.
        :rtype: object
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this EventLogDiagnostics.

        Device characteristics.

        :param device: The device of this EventLogDiagnostics.
        :type device: object
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    @property
    def install_id(self):
        """Gets the install_id of this EventLogDiagnostics.

        Install ID. 

        :return: The install_id of this EventLogDiagnostics.
        :rtype: str
        """
        return self._install_id

    @install_id.setter
    def install_id(self, install_id):
        """Sets the install_id of this EventLogDiagnostics.

        Install ID. 

        :param install_id: The install_id of this EventLogDiagnostics.
        :type install_id: str
        """
        if install_id is None:
            raise ValueError("Invalid value for `install_id`, must not be `None`")

        self._install_id = install_id

    @property
    def timestamp(self):
        """Gets the timestamp of this EventLogDiagnostics.

        Log creation timestamp. 

        :return: The timestamp of this EventLogDiagnostics.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EventLogDiagnostics.

        Log creation timestamp. 

        :param timestamp: The timestamp of this EventLogDiagnostics.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this EventLogDiagnostics.

        Log type. 

        :return: The type of this EventLogDiagnostics.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventLogDiagnostics.

        Log type. 

        :param type: The type of this EventLogDiagnostics.
        :type type: str
        """
        allowed_values = ["event", "page", "start_session", "error", "push_installation", "start_service", "custom_properties"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
