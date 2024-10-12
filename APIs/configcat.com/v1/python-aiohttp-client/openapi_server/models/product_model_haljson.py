# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.config_model_haljson_embedded_product_embedded import ConfigModelHaljsonEmbeddedProductEmbedded
from openapi_server.models.config_model_haljson_embedded_product_links import ConfigModelHaljsonEmbeddedProductLinks
from openapi_server import util


class ProductModelHaljson(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, embedded: ConfigModelHaljsonEmbeddedProductEmbedded=None, links: ConfigModelHaljsonEmbeddedProductLinks=None, description: str=None, name: str=None, order: int=None, product_id: str=None, reason_required: bool=None):
        """ProductModelHaljson - a model defined in OpenAPI

        :param embedded: The embedded of this ProductModelHaljson.
        :param links: The links of this ProductModelHaljson.
        :param description: The description of this ProductModelHaljson.
        :param name: The name of this ProductModelHaljson.
        :param order: The order of this ProductModelHaljson.
        :param product_id: The product_id of this ProductModelHaljson.
        :param reason_required: The reason_required of this ProductModelHaljson.
        """
        self.openapi_types = {
            'embedded': ConfigModelHaljsonEmbeddedProductEmbedded,
            'links': ConfigModelHaljsonEmbeddedProductLinks,
            'description': str,
            'name': str,
            'order': int,
            'product_id': str,
            'reason_required': bool
        }

        self.attribute_map = {
            'embedded': '_embedded',
            'links': '_links',
            'description': 'description',
            'name': 'name',
            'order': 'order',
            'product_id': 'productId',
            'reason_required': 'reasonRequired'
        }

        self._embedded = embedded
        self._links = links
        self._description = description
        self._name = name
        self._order = order
        self._product_id = product_id
        self._reason_required = reason_required

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductModelHaljson':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductModel-haljson of this ProductModelHaljson.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def embedded(self):
        """Gets the embedded of this ProductModelHaljson.


        :return: The embedded of this ProductModelHaljson.
        :rtype: ConfigModelHaljsonEmbeddedProductEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this ProductModelHaljson.


        :param embedded: The embedded of this ProductModelHaljson.
        :type embedded: ConfigModelHaljsonEmbeddedProductEmbedded
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this ProductModelHaljson.


        :return: The links of this ProductModelHaljson.
        :rtype: ConfigModelHaljsonEmbeddedProductLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProductModelHaljson.


        :param links: The links of this ProductModelHaljson.
        :type links: ConfigModelHaljsonEmbeddedProductLinks
        """

        self._links = links

    @property
    def description(self):
        """Gets the description of this ProductModelHaljson.


        :return: The description of this ProductModelHaljson.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductModelHaljson.


        :param description: The description of this ProductModelHaljson.
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ProductModelHaljson.


        :return: The name of this ProductModelHaljson.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductModelHaljson.


        :param name: The name of this ProductModelHaljson.
        :type name: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this ProductModelHaljson.


        :return: The order of this ProductModelHaljson.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ProductModelHaljson.


        :param order: The order of this ProductModelHaljson.
        :type order: int
        """

        self._order = order

    @property
    def product_id(self):
        """Gets the product_id of this ProductModelHaljson.


        :return: The product_id of this ProductModelHaljson.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductModelHaljson.


        :param product_id: The product_id of this ProductModelHaljson.
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def reason_required(self):
        """Gets the reason_required of this ProductModelHaljson.


        :return: The reason_required of this ProductModelHaljson.
        :rtype: bool
        """
        return self._reason_required

    @reason_required.setter
    def reason_required(self, reason_required):
        """Sets the reason_required of this ProductModelHaljson.


        :param reason_required: The reason_required of this ProductModelHaljson.
        :type reason_required: bool
        """

        self._reason_required = reason_required
