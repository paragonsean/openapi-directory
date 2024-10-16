# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.saml_configuration_properties import SamlConfigurationProperties
from openapi_server import util


class SamlConfigurationInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bundle_location: str=None, description: str=None, pid: str=None, properties: SamlConfigurationProperties=None, service_location: str=None, title: str=None):
        """SamlConfigurationInfo - a model defined in OpenAPI

        :param bundle_location: The bundle_location of this SamlConfigurationInfo.
        :param description: The description of this SamlConfigurationInfo.
        :param pid: The pid of this SamlConfigurationInfo.
        :param properties: The properties of this SamlConfigurationInfo.
        :param service_location: The service_location of this SamlConfigurationInfo.
        :param title: The title of this SamlConfigurationInfo.
        """
        self.openapi_types = {
            'bundle_location': str,
            'description': str,
            'pid': str,
            'properties': SamlConfigurationProperties,
            'service_location': str,
            'title': str
        }

        self.attribute_map = {
            'bundle_location': 'bundle_location',
            'description': 'description',
            'pid': 'pid',
            'properties': 'properties',
            'service_location': 'service_location',
            'title': 'title'
        }

        self._bundle_location = bundle_location
        self._description = description
        self._pid = pid
        self._properties = properties
        self._service_location = service_location
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SamlConfigurationInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SamlConfigurationInfo of this SamlConfigurationInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bundle_location(self):
        """Gets the bundle_location of this SamlConfigurationInfo.

        needed for configuration binding

        :return: The bundle_location of this SamlConfigurationInfo.
        :rtype: str
        """
        return self._bundle_location

    @bundle_location.setter
    def bundle_location(self, bundle_location):
        """Sets the bundle_location of this SamlConfigurationInfo.

        needed for configuration binding

        :param bundle_location: The bundle_location of this SamlConfigurationInfo.
        :type bundle_location: str
        """

        self._bundle_location = bundle_location

    @property
    def description(self):
        """Gets the description of this SamlConfigurationInfo.

        Title

        :return: The description of this SamlConfigurationInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SamlConfigurationInfo.

        Title

        :param description: The description of this SamlConfigurationInfo.
        :type description: str
        """

        self._description = description

    @property
    def pid(self):
        """Gets the pid of this SamlConfigurationInfo.

        Persistent Identity (PID)

        :return: The pid of this SamlConfigurationInfo.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this SamlConfigurationInfo.

        Persistent Identity (PID)

        :param pid: The pid of this SamlConfigurationInfo.
        :type pid: str
        """

        self._pid = pid

    @property
    def properties(self):
        """Gets the properties of this SamlConfigurationInfo.


        :return: The properties of this SamlConfigurationInfo.
        :rtype: SamlConfigurationProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SamlConfigurationInfo.


        :param properties: The properties of this SamlConfigurationInfo.
        :type properties: SamlConfigurationProperties
        """

        self._properties = properties

    @property
    def service_location(self):
        """Gets the service_location of this SamlConfigurationInfo.

        needed for configuraiton binding

        :return: The service_location of this SamlConfigurationInfo.
        :rtype: str
        """
        return self._service_location

    @service_location.setter
    def service_location(self, service_location):
        """Sets the service_location of this SamlConfigurationInfo.

        needed for configuraiton binding

        :param service_location: The service_location of this SamlConfigurationInfo.
        :type service_location: str
        """

        self._service_location = service_location

    @property
    def title(self):
        """Gets the title of this SamlConfigurationInfo.

        Title

        :return: The title of this SamlConfigurationInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SamlConfigurationInfo.

        Title

        :param title: The title of this SamlConfigurationInfo.
        :type title: str
        """

        self._title = title
