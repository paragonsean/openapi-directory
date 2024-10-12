# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.gift_card_object import GiftCardObject
from openapi_server.models.pagination import Pagination
from openapi_server import util


class GiftCardObjectListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, resources: List[GiftCardObject]=None):
        """GiftCardObjectListResponse - a model defined in OpenAPI

        :param pagination: The pagination of this GiftCardObjectListResponse.
        :param resources: The resources of this GiftCardObjectListResponse.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'resources': List[GiftCardObject]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'resources': 'resources'
        }

        self._pagination = pagination
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GiftCardObjectListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GiftCardObjectListResponse of this GiftCardObjectListResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this GiftCardObjectListResponse.


        :return: The pagination of this GiftCardObjectListResponse.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this GiftCardObjectListResponse.


        :param pagination: The pagination of this GiftCardObjectListResponse.
        :type pagination: Pagination
        """

        self._pagination = pagination

    @property
    def resources(self):
        """Gets the resources of this GiftCardObjectListResponse.

        Resources corresponding to the list request.

        :return: The resources of this GiftCardObjectListResponse.
        :rtype: List[GiftCardObject]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this GiftCardObjectListResponse.

        Resources corresponding to the list request.

        :param resources: The resources of this GiftCardObjectListResponse.
        :type resources: List[GiftCardObject]
        """

        self._resources = resources
