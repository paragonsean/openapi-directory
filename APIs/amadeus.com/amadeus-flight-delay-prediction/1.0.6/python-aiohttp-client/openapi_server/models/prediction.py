# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_meta_link import CollectionMetaLink
from openapi_server.models.delay_prediction import DelayPrediction
from openapi_server import util


class Prediction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[DelayPrediction]=None, meta: CollectionMetaLink=None):
        """Prediction - a model defined in OpenAPI

        :param data: The data of this Prediction.
        :param meta: The meta of this Prediction.
        """
        self.openapi_types = {
            'data': List[DelayPrediction],
            'meta': CollectionMetaLink
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Prediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Prediction of this Prediction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this Prediction.


        :return: The data of this Prediction.
        :rtype: List[DelayPrediction]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Prediction.


        :param data: The data of this Prediction.
        :type data: List[DelayPrediction]
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this Prediction.


        :return: The meta of this Prediction.
        :rtype: CollectionMetaLink
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Prediction.


        :param meta: The meta of this Prediction.
        :type meta: CollectionMetaLink
        """

        self._meta = meta
