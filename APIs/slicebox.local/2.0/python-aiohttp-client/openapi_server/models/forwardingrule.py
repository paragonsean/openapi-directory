# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.destination import Destination
from openapi_server.models.source import Source
from openapi_server import util


class Forwardingrule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, destination: Destination=None, id: int=None, keep_images: bool=None, source: Source=None):
        """Forwardingrule - a model defined in OpenAPI

        :param destination: The destination of this Forwardingrule.
        :param id: The id of this Forwardingrule.
        :param keep_images: The keep_images of this Forwardingrule.
        :param source: The source of this Forwardingrule.
        """
        self.openapi_types = {
            'destination': Destination,
            'id': int,
            'keep_images': bool,
            'source': Source
        }

        self.attribute_map = {
            'destination': 'destination',
            'id': 'id',
            'keep_images': 'keepImages',
            'source': 'source'
        }

        self._destination = destination
        self._id = id
        self._keep_images = keep_images
        self._source = source

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Forwardingrule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The forwardingrule of this Forwardingrule.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination(self):
        """Gets the destination of this Forwardingrule.


        :return: The destination of this Forwardingrule.
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Forwardingrule.


        :param destination: The destination of this Forwardingrule.
        :type destination: Destination
        """

        self._destination = destination

    @property
    def id(self):
        """Gets the id of this Forwardingrule.


        :return: The id of this Forwardingrule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Forwardingrule.


        :param id: The id of this Forwardingrule.
        :type id: int
        """

        self._id = id

    @property
    def keep_images(self):
        """Gets the keep_images of this Forwardingrule.


        :return: The keep_images of this Forwardingrule.
        :rtype: bool
        """
        return self._keep_images

    @keep_images.setter
    def keep_images(self, keep_images):
        """Sets the keep_images of this Forwardingrule.


        :param keep_images: The keep_images of this Forwardingrule.
        :type keep_images: bool
        """

        self._keep_images = keep_images

    @property
    def source(self):
        """Gets the source of this Forwardingrule.


        :return: The source of this Forwardingrule.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Forwardingrule.


        :param source: The source of this Forwardingrule.
        :type source: Source
        """

        self._source = source
