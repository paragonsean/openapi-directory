# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class V2SymbolStatusEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    MISSING = 'missing'
    IGNORED = 'ignored'
    AVAILABLE = 'available'

    def __init__(self):
        """V2SymbolStatusEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'V2SymbolStatusEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The v2SymbolStatusEnum of this V2SymbolStatusEnum.
        """
        return util.deserialize_model(dikt, cls)
