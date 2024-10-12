# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.offer_object import OfferObject
from openapi_server.models.pagination import Pagination
from openapi_server import util


class OfferObjectListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, resources: List[OfferObject]=None):
        """OfferObjectListResponse - a model defined in OpenAPI

        :param pagination: The pagination of this OfferObjectListResponse.
        :param resources: The resources of this OfferObjectListResponse.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'resources': List[OfferObject]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'resources': 'resources'
        }

        self._pagination = pagination
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OfferObjectListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OfferObjectListResponse of this OfferObjectListResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this OfferObjectListResponse.


        :return: The pagination of this OfferObjectListResponse.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this OfferObjectListResponse.


        :param pagination: The pagination of this OfferObjectListResponse.
        :type pagination: Pagination
        """

        self._pagination = pagination

    @property
    def resources(self):
        """Gets the resources of this OfferObjectListResponse.

        Resources corresponding to the list request.

        :return: The resources of this OfferObjectListResponse.
        :rtype: List[OfferObject]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this OfferObjectListResponse.

        Resources corresponding to the list request.

        :param resources: The resources of this OfferObjectListResponse.
        :type resources: List[OfferObject]
        """

        self._resources = resources
