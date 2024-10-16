# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CodePushDeploymentsUpdateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """CodePushDeploymentsUpdateRequest - a model defined in OpenAPI

        :param name: The name of this CodePushDeploymentsUpdateRequest.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CodePushDeploymentsUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The codePushDeployments_update_request of this CodePushDeploymentsUpdateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CodePushDeploymentsUpdateRequest.


        :return: The name of this CodePushDeploymentsUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodePushDeploymentsUpdateRequest.


        :param name: The name of this CodePushDeploymentsUpdateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 1000:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1000`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name
