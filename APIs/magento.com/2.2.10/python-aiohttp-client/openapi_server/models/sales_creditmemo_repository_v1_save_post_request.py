# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface
from openapi_server import util


class SalesCreditmemoRepositoryV1SavePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity: SalesDataCreditmemoInterface=None):
        """SalesCreditmemoRepositoryV1SavePostRequest - a model defined in OpenAPI

        :param entity: The entity of this SalesCreditmemoRepositoryV1SavePostRequest.
        """
        self.openapi_types = {
            'entity': SalesDataCreditmemoInterface
        }

        self.attribute_map = {
            'entity': 'entity'
        }

        self._entity = entity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesCreditmemoRepositoryV1SavePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The salesCreditmemoRepositoryV1SavePost_request of this SalesCreditmemoRepositoryV1SavePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity(self):
        """Gets the entity of this SalesCreditmemoRepositoryV1SavePostRequest.


        :return: The entity of this SalesCreditmemoRepositoryV1SavePostRequest.
        :rtype: SalesDataCreditmemoInterface
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this SalesCreditmemoRepositoryV1SavePostRequest.


        :param entity: The entity of this SalesCreditmemoRepositoryV1SavePostRequest.
        :type entity: SalesDataCreditmemoInterface
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")

        self._entity = entity
