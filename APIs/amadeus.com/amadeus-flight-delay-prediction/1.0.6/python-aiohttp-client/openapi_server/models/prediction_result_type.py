# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PredictionResultType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    LESS_THAN_30_MINUTES = 'LESS_THAN_30_MINUTES'
    BETWEEN_30_AND_60_MINUTES = 'BETWEEN_30_AND_60_MINUTES'
    BETWEEN_60_AND_120_MINUTES = 'BETWEEN_60_AND_120_MINUTES'
    OVER_120_MINUTES_OR_CANCELLED = 'OVER_120_MINUTES_OR_CANCELLED'

    def __init__(self):
        """PredictionResultType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PredictionResultType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PredictionResultType of this PredictionResultType.
        """
        return util.deserialize_model(dikt, cls)
