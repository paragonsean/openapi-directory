# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SalesDataShipmentCreationArgumentsExtensionInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ext_location_id: str=None, ext_return_shipment_id: str=None, ext_shipment_id: str=None, ext_tracking_reference: str=None, ext_tracking_url: str=None, shipping_label: str=None):
        """SalesDataShipmentCreationArgumentsExtensionInterface - a model defined in OpenAPI

        :param ext_location_id: The ext_location_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :param ext_return_shipment_id: The ext_return_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :param ext_shipment_id: The ext_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :param ext_tracking_reference: The ext_tracking_reference of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :param ext_tracking_url: The ext_tracking_url of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :param shipping_label: The shipping_label of this SalesDataShipmentCreationArgumentsExtensionInterface.
        """
        self.openapi_types = {
            'ext_location_id': str,
            'ext_return_shipment_id': str,
            'ext_shipment_id': str,
            'ext_tracking_reference': str,
            'ext_tracking_url': str,
            'shipping_label': str
        }

        self.attribute_map = {
            'ext_location_id': 'ext_location_id',
            'ext_return_shipment_id': 'ext_return_shipment_id',
            'ext_shipment_id': 'ext_shipment_id',
            'ext_tracking_reference': 'ext_tracking_reference',
            'ext_tracking_url': 'ext_tracking_url',
            'shipping_label': 'shipping_label'
        }

        self._ext_location_id = ext_location_id
        self._ext_return_shipment_id = ext_return_shipment_id
        self._ext_shipment_id = ext_shipment_id
        self._ext_tracking_reference = ext_tracking_reference
        self._ext_tracking_url = ext_tracking_url
        self._shipping_label = shipping_label

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataShipmentCreationArgumentsExtensionInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-shipment-creation-arguments-extension-interface of this SalesDataShipmentCreationArgumentsExtensionInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ext_location_id(self):
        """Gets the ext_location_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The ext_location_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._ext_location_id

    @ext_location_id.setter
    def ext_location_id(self, ext_location_id):
        """Sets the ext_location_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param ext_location_id: The ext_location_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type ext_location_id: str
        """

        self._ext_location_id = ext_location_id

    @property
    def ext_return_shipment_id(self):
        """Gets the ext_return_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The ext_return_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._ext_return_shipment_id

    @ext_return_shipment_id.setter
    def ext_return_shipment_id(self, ext_return_shipment_id):
        """Sets the ext_return_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param ext_return_shipment_id: The ext_return_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type ext_return_shipment_id: str
        """

        self._ext_return_shipment_id = ext_return_shipment_id

    @property
    def ext_shipment_id(self):
        """Gets the ext_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The ext_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._ext_shipment_id

    @ext_shipment_id.setter
    def ext_shipment_id(self, ext_shipment_id):
        """Sets the ext_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param ext_shipment_id: The ext_shipment_id of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type ext_shipment_id: str
        """

        self._ext_shipment_id = ext_shipment_id

    @property
    def ext_tracking_reference(self):
        """Gets the ext_tracking_reference of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The ext_tracking_reference of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._ext_tracking_reference

    @ext_tracking_reference.setter
    def ext_tracking_reference(self, ext_tracking_reference):
        """Sets the ext_tracking_reference of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param ext_tracking_reference: The ext_tracking_reference of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type ext_tracking_reference: str
        """

        self._ext_tracking_reference = ext_tracking_reference

    @property
    def ext_tracking_url(self):
        """Gets the ext_tracking_url of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The ext_tracking_url of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._ext_tracking_url

    @ext_tracking_url.setter
    def ext_tracking_url(self, ext_tracking_url):
        """Sets the ext_tracking_url of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param ext_tracking_url: The ext_tracking_url of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type ext_tracking_url: str
        """

        self._ext_tracking_url = ext_tracking_url

    @property
    def shipping_label(self):
        """Gets the shipping_label of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :return: The shipping_label of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :rtype: str
        """
        return self._shipping_label

    @shipping_label.setter
    def shipping_label(self, shipping_label):
        """Sets the shipping_label of this SalesDataShipmentCreationArgumentsExtensionInterface.


        :param shipping_label: The shipping_label of this SalesDataShipmentCreationArgumentsExtensionInterface.
        :type shipping_label: str
        """

        self._shipping_label = shipping_label
