# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.action_metric_validations_maximum import ActionMetricValidationsMaximum
from openapi_server import util


class ActionMetricValidations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, maximum: ActionMetricValidationsMaximum=None, minimum: ActionMetricValidationsMaximum=None):
        """ActionMetricValidations - a model defined in OpenAPI

        :param maximum: The maximum of this ActionMetricValidations.
        :param minimum: The minimum of this ActionMetricValidations.
        """
        self.openapi_types = {
            'maximum': ActionMetricValidationsMaximum,
            'minimum': ActionMetricValidationsMaximum
        }

        self.attribute_map = {
            'maximum': 'maximum',
            'minimum': 'minimum'
        }

        self._maximum = maximum
        self._minimum = minimum

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ActionMetricValidations':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ActionMetric_validations of this ActionMetricValidations.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def maximum(self):
        """Gets the maximum of this ActionMetricValidations.


        :return: The maximum of this ActionMetricValidations.
        :rtype: ActionMetricValidationsMaximum
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this ActionMetricValidations.


        :param maximum: The maximum of this ActionMetricValidations.
        :type maximum: ActionMetricValidationsMaximum
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this ActionMetricValidations.


        :return: The minimum of this ActionMetricValidations.
        :rtype: ActionMetricValidationsMaximum
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this ActionMetricValidations.


        :param minimum: The minimum of this ActionMetricValidations.
        :type minimum: ActionMetricValidationsMaximum
        """

        self._minimum = minimum
