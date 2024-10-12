# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server import util


class CatalogProductCustomOptionRepositoryV1SavePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, option: CatalogDataProductCustomOptionInterface=None):
        """CatalogProductCustomOptionRepositoryV1SavePostRequest - a model defined in OpenAPI

        :param option: The option of this CatalogProductCustomOptionRepositoryV1SavePostRequest.
        """
        self.openapi_types = {
            'option': CatalogDataProductCustomOptionInterface
        }

        self.attribute_map = {
            'option': 'option'
        }

        self._option = option

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogProductCustomOptionRepositoryV1SavePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalogProductCustomOptionRepositoryV1SavePost_request of this CatalogProductCustomOptionRepositoryV1SavePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def option(self):
        """Gets the option of this CatalogProductCustomOptionRepositoryV1SavePostRequest.


        :return: The option of this CatalogProductCustomOptionRepositoryV1SavePostRequest.
        :rtype: CatalogDataProductCustomOptionInterface
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this CatalogProductCustomOptionRepositoryV1SavePostRequest.


        :param option: The option of this CatalogProductCustomOptionRepositoryV1SavePostRequest.
        :type option: CatalogDataProductCustomOptionInterface
        """
        if option is None:
            raise ValueError("Invalid value for `option`, must not be `None`")

        self._option = option
