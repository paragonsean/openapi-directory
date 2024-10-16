# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.outgoing_image import OutgoingImage
from openapi_server.models.outgoing_transaction import OutgoingTransaction
from openapi_server import util


class OutgoingTransactionImage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image: OutgoingImage=None, transaction: OutgoingTransaction=None):
        """OutgoingTransactionImage - a model defined in OpenAPI

        :param image: The image of this OutgoingTransactionImage.
        :param transaction: The transaction of this OutgoingTransactionImage.
        """
        self.openapi_types = {
            'image': OutgoingImage,
            'transaction': OutgoingTransaction
        }

        self.attribute_map = {
            'image': 'image',
            'transaction': 'transaction'
        }

        self._image = image
        self._transaction = transaction

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutgoingTransactionImage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The outgoingTransactionImage of this OutgoingTransactionImage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self):
        """Gets the image of this OutgoingTransactionImage.


        :return: The image of this OutgoingTransactionImage.
        :rtype: OutgoingImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this OutgoingTransactionImage.


        :param image: The image of this OutgoingTransactionImage.
        :type image: OutgoingImage
        """

        self._image = image

    @property
    def transaction(self):
        """Gets the transaction of this OutgoingTransactionImage.


        :return: The transaction of this OutgoingTransactionImage.
        :rtype: OutgoingTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this OutgoingTransactionImage.


        :param transaction: The transaction of this OutgoingTransactionImage.
        :type transaction: OutgoingTransaction
        """

        self._transaction = transaction
