# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JurisdictionClassification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    STATE = 'state'
    MUNICIPALITY = 'municipality'
    COUNTRY = 'country'

    def __init__(self):
        """JurisdictionClassification - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JurisdictionClassification':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JurisdictionClassification of this JurisdictionClassification.
        """
        return util.deserialize_model(dikt, cls)
