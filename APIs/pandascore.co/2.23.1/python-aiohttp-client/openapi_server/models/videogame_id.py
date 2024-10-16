# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VideogameID(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NUMBER_1 = 1
    NUMBER_3 = 3
    NUMBER_4 = 4
    NUMBER_14 = 14
    NUMBER_20 = 20
    NUMBER_22 = 22
    NUMBER_23 = 23
    NUMBER_24 = 24
    NUMBER_25 = 25
    NUMBER_26 = 26

    def __init__(self):
        """VideogameID - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VideogameID':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VideogameID of this VideogameID.
        """
        return util.deserialize_model(dikt, cls)
