# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PluginMount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, destination: str=None, name: str=None, options: List[str]=None, settable: List[str]=None, source: str=None, type: str=None):
        """PluginMount - a model defined in OpenAPI

        :param description: The description of this PluginMount.
        :param destination: The destination of this PluginMount.
        :param name: The name of this PluginMount.
        :param options: The options of this PluginMount.
        :param settable: The settable of this PluginMount.
        :param source: The source of this PluginMount.
        :param type: The type of this PluginMount.
        """
        self.openapi_types = {
            'description': str,
            'destination': str,
            'name': str,
            'options': List[str],
            'settable': List[str],
            'source': str,
            'type': str
        }

        self.attribute_map = {
            'description': 'Description',
            'destination': 'Destination',
            'name': 'Name',
            'options': 'Options',
            'settable': 'Settable',
            'source': 'Source',
            'type': 'Type'
        }

        self._description = description
        self._destination = destination
        self._name = name
        self._options = options
        self._settable = settable
        self._source = source
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PluginMount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PluginMount of this PluginMount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this PluginMount.

        description

        :return: The description of this PluginMount.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PluginMount.

        description

        :param description: The description of this PluginMount.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def destination(self):
        """Gets the destination of this PluginMount.

        destination

        :return: The destination of this PluginMount.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this PluginMount.

        destination

        :param destination: The destination of this PluginMount.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")

        self._destination = destination

    @property
    def name(self):
        """Gets the name of this PluginMount.

        name

        :return: The name of this PluginMount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginMount.

        name

        :param name: The name of this PluginMount.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def options(self):
        """Gets the options of this PluginMount.

        options

        :return: The options of this PluginMount.
        :rtype: List[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PluginMount.

        options

        :param options: The options of this PluginMount.
        :type options: List[str]
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")

        self._options = options

    @property
    def settable(self):
        """Gets the settable of this PluginMount.

        settable

        :return: The settable of this PluginMount.
        :rtype: List[str]
        """
        return self._settable

    @settable.setter
    def settable(self, settable):
        """Sets the settable of this PluginMount.

        settable

        :param settable: The settable of this PluginMount.
        :type settable: List[str]
        """
        if settable is None:
            raise ValueError("Invalid value for `settable`, must not be `None`")

        self._settable = settable

    @property
    def source(self):
        """Gets the source of this PluginMount.

        source

        :return: The source of this PluginMount.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PluginMount.

        source

        :param source: The source of this PluginMount.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def type(self):
        """Gets the type of this PluginMount.

        type

        :return: The type of this PluginMount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PluginMount.

        type

        :param type: The type of this PluginMount.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
