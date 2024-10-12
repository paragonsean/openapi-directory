# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GalleryImageReference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offer: str=None, os_type: str=None, publisher: str=None, sku: str=None, version: str=None):
        """GalleryImageReference - a model defined in OpenAPI

        :param offer: The offer of this GalleryImageReference.
        :param os_type: The os_type of this GalleryImageReference.
        :param publisher: The publisher of this GalleryImageReference.
        :param sku: The sku of this GalleryImageReference.
        :param version: The version of this GalleryImageReference.
        """
        self.openapi_types = {
            'offer': str,
            'os_type': str,
            'publisher': str,
            'sku': str,
            'version': str
        }

        self.attribute_map = {
            'offer': 'offer',
            'os_type': 'osType',
            'publisher': 'publisher',
            'sku': 'sku',
            'version': 'version'
        }

        self._offer = offer
        self._os_type = os_type
        self._publisher = publisher
        self._sku = sku
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GalleryImageReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GalleryImageReference of this GalleryImageReference.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offer(self):
        """Gets the offer of this GalleryImageReference.

        The offer of the gallery image.

        :return: The offer of this GalleryImageReference.
        :rtype: str
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this GalleryImageReference.

        The offer of the gallery image.

        :param offer: The offer of this GalleryImageReference.
        :type offer: str
        """

        self._offer = offer

    @property
    def os_type(self):
        """Gets the os_type of this GalleryImageReference.

        The OS type of the gallery image.

        :return: The os_type of this GalleryImageReference.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this GalleryImageReference.

        The OS type of the gallery image.

        :param os_type: The os_type of this GalleryImageReference.
        :type os_type: str
        """

        self._os_type = os_type

    @property
    def publisher(self):
        """Gets the publisher of this GalleryImageReference.

        The publisher of the gallery image.

        :return: The publisher of this GalleryImageReference.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this GalleryImageReference.

        The publisher of the gallery image.

        :param publisher: The publisher of this GalleryImageReference.
        :type publisher: str
        """

        self._publisher = publisher

    @property
    def sku(self):
        """Gets the sku of this GalleryImageReference.

        The SKU of the gallery image.

        :return: The sku of this GalleryImageReference.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this GalleryImageReference.

        The SKU of the gallery image.

        :param sku: The sku of this GalleryImageReference.
        :type sku: str
        """

        self._sku = sku

    @property
    def version(self):
        """Gets the version of this GalleryImageReference.

        The version of the gallery image.

        :return: The version of this GalleryImageReference.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GalleryImageReference.

        The version of the gallery image.

        :param version: The version of this GalleryImageReference.
        :type version: str
        """

        self._version = version
