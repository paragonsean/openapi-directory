# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ServiceRole(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    HIP = 'HIP'
    HIU = 'HIU'
    HIP_AND_HIU = 'HIP_AND_HIU'
    HEALTH_LOCKER = 'HEALTH_LOCKER'

    def __init__(self):
        """ServiceRole - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServiceRole':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceRole of this ServiceRole.
        """
        return util.deserialize_model(dikt, cls)
