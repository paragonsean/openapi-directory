# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_core_requests_patch_body import ApiCoreRequestsPatchBody
from openapi_server import util


class ApiCoreRequestsPatchBodyBatch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, patch_requests: List[ApiCoreRequestsPatchBody]=None):
        """ApiCoreRequestsPatchBodyBatch - a model defined in OpenAPI

        :param patch_requests: The patch_requests of this ApiCoreRequestsPatchBodyBatch.
        """
        self.openapi_types = {
            'patch_requests': List[ApiCoreRequestsPatchBody]
        }

        self.attribute_map = {
            'patch_requests': 'PatchRequests'
        }

        self._patch_requests = patch_requests

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreRequestsPatchBodyBatch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Requests.PatchBodyBatch of this ApiCoreRequestsPatchBodyBatch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def patch_requests(self):
        """Gets the patch_requests of this ApiCoreRequestsPatchBodyBatch.


        :return: The patch_requests of this ApiCoreRequestsPatchBodyBatch.
        :rtype: List[ApiCoreRequestsPatchBody]
        """
        return self._patch_requests

    @patch_requests.setter
    def patch_requests(self, patch_requests):
        """Sets the patch_requests of this ApiCoreRequestsPatchBodyBatch.


        :param patch_requests: The patch_requests of this ApiCoreRequestsPatchBodyBatch.
        :type patch_requests: List[ApiCoreRequestsPatchBody]
        """

        self._patch_requests = patch_requests
