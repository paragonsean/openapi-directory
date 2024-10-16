# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner_conditions_inner_threshold_noise_ambient import GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient
from openapi_server import util


class GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ambient: GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient=None):
        """GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise - a model defined in OpenAPI

        :param ambient: The ambient of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.
        """
        self.openapi_types = {
            'ambient': GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient
        }

        self.attribute_map = {
            'ambient': 'ambient'
        }

        self._ambient = ambient

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSensorAlertsProfiles_200_response_inner_conditions_inner_threshold_noise of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ambient(self):
        """Gets the ambient of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.


        :return: The ambient of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.
        :rtype: GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient
        """
        return self._ambient

    @ambient.setter
    def ambient(self, ambient):
        """Sets the ambient of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.


        :param ambient: The ambient of this GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.
        :type ambient: GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient
        """
        if ambient is None:
            raise ValueError("Invalid value for `ambient`, must not be `None`")

        self._ambient = ambient
