# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Trend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DOWN = 'DOWN'
    LOW_DOWN = 'LOW_DOWN'
    STABLE = 'STABLE'
    LOW_UP = 'LOW_UP'
    UP = 'UP'

    def __init__(self):
        """Trend - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Trend':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Trend of this Trend.
        """
        return util.deserialize_model(dikt, cls)
