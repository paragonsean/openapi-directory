# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class HealthProfileAnswerResourceAttributesLatest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_by: str=None, answered_at: str=None, value: str=None):
        """HealthProfileAnswerResourceAttributesLatest - a model defined in OpenAPI

        :param created_by: The created_by of this HealthProfileAnswerResourceAttributesLatest.
        :param answered_at: The answered_at of this HealthProfileAnswerResourceAttributesLatest.
        :param value: The value of this HealthProfileAnswerResourceAttributesLatest.
        """
        self.openapi_types = {
            'created_by': str,
            'answered_at': str,
            'value': str
        }

        self.attribute_map = {
            'created_by': '_created_by',
            'answered_at': 'answered_at',
            'value': 'value'
        }

        self._created_by = created_by
        self._answered_at = answered_at
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HealthProfileAnswerResourceAttributesLatest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthProfileAnswerResource_attributes_latest of this HealthProfileAnswerResourceAttributesLatest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_by(self):
        """Gets the created_by of this HealthProfileAnswerResourceAttributesLatest.

        The id of the patient or coach who answered the health profile question

        :return: The created_by of this HealthProfileAnswerResourceAttributesLatest.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this HealthProfileAnswerResourceAttributesLatest.

        The id of the patient or coach who answered the health profile question

        :param created_by: The created_by of this HealthProfileAnswerResourceAttributesLatest.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def answered_at(self):
        """Gets the answered_at of this HealthProfileAnswerResourceAttributesLatest.

        The date when the health profile question is answered

        :return: The answered_at of this HealthProfileAnswerResourceAttributesLatest.
        :rtype: str
        """
        return self._answered_at

    @answered_at.setter
    def answered_at(self, answered_at):
        """Sets the answered_at of this HealthProfileAnswerResourceAttributesLatest.

        The date when the health profile question is answered

        :param answered_at: The answered_at of this HealthProfileAnswerResourceAttributesLatest.
        :type answered_at: str
        """

        self._answered_at = answered_at

    @property
    def value(self):
        """Gets the value of this HealthProfileAnswerResourceAttributesLatest.

        The value of the answer entered for the health profile question

        :return: The value of this HealthProfileAnswerResourceAttributesLatest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this HealthProfileAnswerResourceAttributesLatest.

        The value of the answer entered for the health profile question

        :param value: The value of this HealthProfileAnswerResourceAttributesLatest.
        :type value: str
        """

        self._value = value
