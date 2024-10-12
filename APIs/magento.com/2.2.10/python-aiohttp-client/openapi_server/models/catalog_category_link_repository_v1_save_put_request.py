# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.catalog_data_category_product_link_interface import CatalogDataCategoryProductLinkInterface
from openapi_server import util


class CatalogCategoryLinkRepositoryV1SavePutRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, product_link: CatalogDataCategoryProductLinkInterface=None):
        """CatalogCategoryLinkRepositoryV1SavePutRequest - a model defined in OpenAPI

        :param product_link: The product_link of this CatalogCategoryLinkRepositoryV1SavePutRequest.
        """
        self.openapi_types = {
            'product_link': CatalogDataCategoryProductLinkInterface
        }

        self.attribute_map = {
            'product_link': 'productLink'
        }

        self._product_link = product_link

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogCategoryLinkRepositoryV1SavePutRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalogCategoryLinkRepositoryV1SavePut_request of this CatalogCategoryLinkRepositoryV1SavePutRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product_link(self):
        """Gets the product_link of this CatalogCategoryLinkRepositoryV1SavePutRequest.


        :return: The product_link of this CatalogCategoryLinkRepositoryV1SavePutRequest.
        :rtype: CatalogDataCategoryProductLinkInterface
        """
        return self._product_link

    @product_link.setter
    def product_link(self, product_link):
        """Sets the product_link of this CatalogCategoryLinkRepositoryV1SavePutRequest.


        :param product_link: The product_link of this CatalogCategoryLinkRepositoryV1SavePutRequest.
        :type product_link: CatalogDataCategoryProductLinkInterface
        """
        if product_link is None:
            raise ValueError("Invalid value for `product_link`, must not be `None`")

        self._product_link = product_link
