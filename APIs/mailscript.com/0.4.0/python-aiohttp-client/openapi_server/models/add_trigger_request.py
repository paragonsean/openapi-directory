# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.add_trigger_request_criteria import AddTriggerRequestCriteria
from openapi_server import util


class AddTriggerRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, criteria: AddTriggerRequestCriteria=None, name: str=None):
        """AddTriggerRequest - a model defined in OpenAPI

        :param criteria: The criteria of this AddTriggerRequest.
        :param name: The name of this AddTriggerRequest.
        """
        self.openapi_types = {
            'criteria': AddTriggerRequestCriteria,
            'name': str
        }

        self.attribute_map = {
            'criteria': 'criteria',
            'name': 'name'
        }

        self._criteria = criteria
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddTriggerRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AddTriggerRequest of this AddTriggerRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def criteria(self):
        """Gets the criteria of this AddTriggerRequest.


        :return: The criteria of this AddTriggerRequest.
        :rtype: AddTriggerRequestCriteria
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this AddTriggerRequest.


        :param criteria: The criteria of this AddTriggerRequest.
        :type criteria: AddTriggerRequestCriteria
        """
        if criteria is None:
            raise ValueError("Invalid value for `criteria`, must not be `None`")

        self._criteria = criteria

    @property
    def name(self):
        """Gets the name of this AddTriggerRequest.


        :return: The name of this AddTriggerRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddTriggerRequest.


        :param name: The name of this AddTriggerRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
