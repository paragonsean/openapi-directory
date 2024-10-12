# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SalesDataShipmentTrackCreationInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, carrier_code: str=None, extension_attributes: object=None, title: str=None, track_number: str=None):
        """SalesDataShipmentTrackCreationInterface - a model defined in OpenAPI

        :param carrier_code: The carrier_code of this SalesDataShipmentTrackCreationInterface.
        :param extension_attributes: The extension_attributes of this SalesDataShipmentTrackCreationInterface.
        :param title: The title of this SalesDataShipmentTrackCreationInterface.
        :param track_number: The track_number of this SalesDataShipmentTrackCreationInterface.
        """
        self.openapi_types = {
            'carrier_code': str,
            'extension_attributes': object,
            'title': str,
            'track_number': str
        }

        self.attribute_map = {
            'carrier_code': 'carrier_code',
            'extension_attributes': 'extension_attributes',
            'title': 'title',
            'track_number': 'track_number'
        }

        self._carrier_code = carrier_code
        self._extension_attributes = extension_attributes
        self._title = title
        self._track_number = track_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataShipmentTrackCreationInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-shipment-track-creation-interface of this SalesDataShipmentTrackCreationInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def carrier_code(self):
        """Gets the carrier_code of this SalesDataShipmentTrackCreationInterface.

        Carrier code.

        :return: The carrier_code of this SalesDataShipmentTrackCreationInterface.
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this SalesDataShipmentTrackCreationInterface.

        Carrier code.

        :param carrier_code: The carrier_code of this SalesDataShipmentTrackCreationInterface.
        :type carrier_code: str
        """
        if carrier_code is None:
            raise ValueError("Invalid value for `carrier_code`, must not be `None`")

        self._carrier_code = carrier_code

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this SalesDataShipmentTrackCreationInterface.

        ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentTrackCreationInterface

        :return: The extension_attributes of this SalesDataShipmentTrackCreationInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this SalesDataShipmentTrackCreationInterface.

        ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentTrackCreationInterface

        :param extension_attributes: The extension_attributes of this SalesDataShipmentTrackCreationInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def title(self):
        """Gets the title of this SalesDataShipmentTrackCreationInterface.

        Title.

        :return: The title of this SalesDataShipmentTrackCreationInterface.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SalesDataShipmentTrackCreationInterface.

        Title.

        :param title: The title of this SalesDataShipmentTrackCreationInterface.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def track_number(self):
        """Gets the track_number of this SalesDataShipmentTrackCreationInterface.

        Track number.

        :return: The track_number of this SalesDataShipmentTrackCreationInterface.
        :rtype: str
        """
        return self._track_number

    @track_number.setter
    def track_number(self, track_number):
        """Sets the track_number of this SalesDataShipmentTrackCreationInterface.

        Track number.

        :param track_number: The track_number of this SalesDataShipmentTrackCreationInterface.
        :type track_number: str
        """
        if track_number is None:
            raise ValueError("Invalid value for `track_number`, must not be `None`")

        self._track_number = track_number
