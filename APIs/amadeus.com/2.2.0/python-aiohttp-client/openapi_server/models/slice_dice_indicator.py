# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SliceDiceIndicator(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    LOCAL_AVAILABILITY = 'LOCAL_AVAILABILITY'
    SUB_OD_AVAILABILITY_1 = 'SUB_OD_AVAILABILITY_1'
    SUB_OD_AVAILABILITY_2 = 'SUB_OD_AVAILABILITY_2'

    def __init__(self):
        """SliceDiceIndicator - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SliceDiceIndicator':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SliceDiceIndicator of this SliceDiceIndicator.
        """
        return util.deserialize_model(dikt, cls)
