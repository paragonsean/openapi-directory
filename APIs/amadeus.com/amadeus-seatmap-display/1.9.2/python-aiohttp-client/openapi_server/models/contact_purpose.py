# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ContactPurpose(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    STANDARD = 'STANDARD'
    INVOICE = 'INVOICE'
    STANDARD_WITHOUT_TRANSMISSION = 'STANDARD_WITHOUT_TRANSMISSION'

    def __init__(self):
        """ContactPurpose - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContactPurpose':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContactPurpose of this ContactPurpose.
        """
        return util.deserialize_model(dikt, cls)
