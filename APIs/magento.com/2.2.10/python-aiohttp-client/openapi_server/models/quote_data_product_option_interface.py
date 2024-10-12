# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.quote_data_product_option_extension_interface import QuoteDataProductOptionExtensionInterface
from openapi_server import util


class QuoteDataProductOptionInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extension_attributes: QuoteDataProductOptionExtensionInterface=None):
        """QuoteDataProductOptionInterface - a model defined in OpenAPI

        :param extension_attributes: The extension_attributes of this QuoteDataProductOptionInterface.
        """
        self.openapi_types = {
            'extension_attributes': QuoteDataProductOptionExtensionInterface
        }

        self.attribute_map = {
            'extension_attributes': 'extension_attributes'
        }

        self._extension_attributes = extension_attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QuoteDataProductOptionInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The quote-data-product-option-interface of this QuoteDataProductOptionInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this QuoteDataProductOptionInterface.


        :return: The extension_attributes of this QuoteDataProductOptionInterface.
        :rtype: QuoteDataProductOptionExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this QuoteDataProductOptionInterface.


        :param extension_attributes: The extension_attributes of this QuoteDataProductOptionInterface.
        :type extension_attributes: QuoteDataProductOptionExtensionInterface
        """

        self._extension_attributes = extension_attributes
