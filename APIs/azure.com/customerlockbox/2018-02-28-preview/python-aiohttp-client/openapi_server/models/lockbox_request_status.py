# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LockboxRequestStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    INITIALIZING = 'Initializing'
    PENDING = 'Pending'
    APPROVING = 'Approving'
    DENYING = 'Denying'
    APPROVED = 'Approved'
    DENIED = 'Denied'
    EXPIRED = 'Expired'
    REVOKING = 'Revoking'
    REVOKED = 'Revoked'
    ERROR = 'Error'
    UNKNOWN = 'Unknown'
    COMPLETED = 'Completed'
    COMPLETING = 'Completing'

    def __init__(self):
        """LockboxRequestStatus - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LockboxRequestStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LockboxRequestStatus of this LockboxRequestStatus.
        """
        return util.deserialize_model(dikt, cls)
