# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserReportType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    MALICIOUSIP = 'MaliciousIP'
    SPAMMING = 'Spamming'
    REMOVEPERMISSIONS = 'RemovePermissions'
    OTHER = 'Other'

    def __init__(self):
        """UserReportType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserReportType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserReportType of this UserReportType.
        """
        return util.deserialize_model(dikt, cls)
