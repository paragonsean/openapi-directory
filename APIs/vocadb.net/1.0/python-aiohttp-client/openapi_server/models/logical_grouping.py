# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LogicalGrouping(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AND = 'And'
    OR = 'Or'

    def __init__(self):
        """LogicalGrouping - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LogicalGrouping':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LogicalGrouping of this LogicalGrouping.
        """
        return util.deserialize_model(dikt, cls)
