# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.feature import Feature
from openapi_server import util


class AddClutterRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, features: List[Feature]=None, name: str='Clutter', type: str='FeatureCollection'):
        """AddClutterRequest - a model defined in OpenAPI

        :param features: The features of this AddClutterRequest.
        :param name: The name of this AddClutterRequest.
        :param type: The type of this AddClutterRequest.
        """
        self.openapi_types = {
            'features': List[Feature],
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'features': 'features',
            'name': 'name',
            'type': 'type'
        }

        self._features = features
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddClutterRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The addClutter_request of this AddClutterRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def features(self):
        """Gets the features of this AddClutterRequest.


        :return: The features of this AddClutterRequest.
        :rtype: List[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AddClutterRequest.


        :param features: The features of this AddClutterRequest.
        :type features: List[Feature]
        """

        self._features = features

    @property
    def name(self):
        """Gets the name of this AddClutterRequest.


        :return: The name of this AddClutterRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddClutterRequest.


        :param name: The name of this AddClutterRequest.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this AddClutterRequest.


        :return: The type of this AddClutterRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddClutterRequest.


        :param type: The type of this AddClutterRequest.
        :type type: str
        """

        self._type = type
