# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class XOriginPoint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2

    def __init__(self):
        """XOriginPoint - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'XOriginPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The XOriginPoint of this XOriginPoint.
        """
        return util.deserialize_model(dikt, cls)
