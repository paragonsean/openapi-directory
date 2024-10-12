# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MessageCode400PIIS(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    FORMAT_ERROR = 'FORMAT_ERROR'
    PARAMETER_NOT_CONSISTENT = 'PARAMETER_NOT_CONSISTENT'
    PARAMETER_NOT_SUPPORTED = 'PARAMETER_NOT_SUPPORTED'
    SERVICE_INVALID = 'SERVICE_INVALID'
    RESOURCE_UNKNOWN = 'RESOURCE_UNKNOWN'
    RESOURCE_EXPIRED = 'RESOURCE_EXPIRED'
    RESOURCE_BLOCKED = 'RESOURCE_BLOCKED'
    TIMESTAMP_INVALID = 'TIMESTAMP_INVALID'
    PERIOD_INVALID = 'PERIOD_INVALID'
    SCA_METHOD_UNKNOWN = 'SCA_METHOD_UNKNOWN'
    SCA_INVALID = 'SCA_INVALID'
    CONSENT_UNKNOWN = 'CONSENT_UNKNOWN'
    CARD_INVALID = 'CARD_INVALID'
    NO_PIIS_ACTIVATION = 'NO_PIIS_ACTIVATION'

    def __init__(self):
        """MessageCode400PIIS - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MessageCode400PIIS':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MessageCode400_PIIS of this MessageCode400PIIS.
        """
        return util.deserialize_model(dikt, cls)
