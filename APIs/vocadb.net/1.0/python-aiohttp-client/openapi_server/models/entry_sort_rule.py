# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EntrySortRule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NONE = 'None'
    NAME = 'Name'
    ADDITIONDATE = 'AdditionDate'
    ACTIVITYDATE = 'ActivityDate'

    def __init__(self):
        """EntrySortRule - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EntrySortRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EntrySortRule of this EntrySortRule.
        """
        return util.deserialize_model(dikt, cls)
