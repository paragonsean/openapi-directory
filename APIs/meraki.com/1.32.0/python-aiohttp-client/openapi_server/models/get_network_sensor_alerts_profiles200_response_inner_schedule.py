# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSensorAlertsProfiles200ResponseInnerSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None):
        """GetNetworkSensorAlertsProfiles200ResponseInnerSchedule - a model defined in OpenAPI

        :param id: The id of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        :param name: The name of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        """
        self.openapi_types = {
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSensorAlertsProfiles200ResponseInnerSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSensorAlertsProfiles_200_response_inner_schedule of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.

        ID of the sensor schedule to use with the alert profile. If not defined, the alert profile will be active at all times.

        :return: The id of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.

        ID of the sensor schedule to use with the alert profile. If not defined, the alert profile will be active at all times.

        :param id: The id of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.

        Name of the sensor schedule to use with the alert profile.

        :return: The name of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.

        Name of the sensor schedule to use with the alert profile.

        :param name: The name of this GetNetworkSensorAlertsProfiles200ResponseInnerSchedule.
        :type name: str
        """

        self._name = name
