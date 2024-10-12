# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MessageCode409PIIS(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    STATUS_INVALID = 'STATUS_INVALID'

    def __init__(self):
        """MessageCode409PIIS - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MessageCode409PIIS':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MessageCode409_PIIS of this MessageCode409PIIS.
        """
        return util.deserialize_model(dikt, cls)
