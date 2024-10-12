# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.matrix_response_hints_inner import MatrixResponseHintsInner
from openapi_server.models.response_info import ResponseInfo
from openapi_server import util


class MatrixResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, distances: List[List[float]]=None, hints: List[MatrixResponseHintsInner]=None, info: ResponseInfo=None, times: List[List[float]]=None, weights: List[List[float]]=None):
        """MatrixResponse - a model defined in OpenAPI

        :param distances: The distances of this MatrixResponse.
        :param hints: The hints of this MatrixResponse.
        :param info: The info of this MatrixResponse.
        :param times: The times of this MatrixResponse.
        :param weights: The weights of this MatrixResponse.
        """
        self.openapi_types = {
            'distances': List[List[float]],
            'hints': List[MatrixResponseHintsInner],
            'info': ResponseInfo,
            'times': List[List[float]],
            'weights': List[List[float]]
        }

        self.attribute_map = {
            'distances': 'distances',
            'hints': 'hints',
            'info': 'info',
            'times': 'times',
            'weights': 'weights'
        }

        self._distances = distances
        self._hints = hints
        self._info = info
        self._times = times
        self._weights = weights

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MatrixResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MatrixResponse of this MatrixResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def distances(self):
        """Gets the distances of this MatrixResponse.

        The distance matrix for the specified points in the same order as the time matrix. The distances are in meters. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :return: The distances of this MatrixResponse.
        :rtype: List[List[float]]
        """
        return self._distances

    @distances.setter
    def distances(self, distances):
        """Sets the distances of this MatrixResponse.

        The distance matrix for the specified points in the same order as the time matrix. The distances are in meters. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :param distances: The distances of this MatrixResponse.
        :type distances: List[List[float]]
        """

        self._distances = distances

    @property
    def hints(self):
        """Gets the hints of this MatrixResponse.

        Optional. Additional response data.

        :return: The hints of this MatrixResponse.
        :rtype: List[MatrixResponseHintsInner]
        """
        return self._hints

    @hints.setter
    def hints(self, hints):
        """Sets the hints of this MatrixResponse.

        Optional. Additional response data.

        :param hints: The hints of this MatrixResponse.
        :type hints: List[MatrixResponseHintsInner]
        """

        self._hints = hints

    @property
    def info(self):
        """Gets the info of this MatrixResponse.


        :return: The info of this MatrixResponse.
        :rtype: ResponseInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this MatrixResponse.


        :param info: The info of this MatrixResponse.
        :type info: ResponseInfo
        """

        self._info = info

    @property
    def times(self):
        """Gets the times of this MatrixResponse.

        The time matrix for the specified points in the order [[from1->to1, from1->to2, ...], [from2->to1, from2->to2, ...], ...]. The times are in seconds. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :return: The times of this MatrixResponse.
        :rtype: List[List[float]]
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this MatrixResponse.

        The time matrix for the specified points in the order [[from1->to1, from1->to2, ...], [from2->to1, from2->to2, ...], ...]. The times are in seconds. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :param times: The times of this MatrixResponse.
        :type times: List[List[float]]
        """

        self._times = times

    @property
    def weights(self):
        """Gets the weights of this MatrixResponse.

        The weight matrix for the specified points in the same order as the time matrix. The weights for different vehicles can have a different unit but the weights array is perfectly suited as input for Vehicle Routing Problems as it is currently faster to calculate. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :return: The weights of this MatrixResponse.
        :rtype: List[List[float]]
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """Sets the weights of this MatrixResponse.

        The weight matrix for the specified points in the same order as the time matrix. The weights for different vehicles can have a different unit but the weights array is perfectly suited as input for Vehicle Routing Problems as it is currently faster to calculate. If `fail_fast=false` the matrix will contain `null` for connections that could not be found.

        :param weights: The weights of this MatrixResponse.
        :type weights: List[List[float]]
        """

        self._weights = weights
