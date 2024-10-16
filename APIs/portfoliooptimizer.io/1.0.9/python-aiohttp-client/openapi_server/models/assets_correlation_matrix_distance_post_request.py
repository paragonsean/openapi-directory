# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AssetsCorrelationMatrixDistancePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: int=None, assets_correlation_matrix: List[List[float]]=None, distance_metric: str='euclidean', reference_correlation_matrix: List[List[float]]=None):
        """AssetsCorrelationMatrixDistancePostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsCorrelationMatrixDistancePostRequest.
        :param assets_correlation_matrix: The assets_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        :param distance_metric: The distance_metric of this AssetsCorrelationMatrixDistancePostRequest.
        :param reference_correlation_matrix: The reference_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        """
        self.openapi_types = {
            'assets': int,
            'assets_correlation_matrix': List[List[float]],
            'distance_metric': str,
            'reference_correlation_matrix': List[List[float]]
        }

        self.attribute_map = {
            'assets': 'assets',
            'assets_correlation_matrix': 'assetsCorrelationMatrix',
            'distance_metric': 'distanceMetric',
            'reference_correlation_matrix': 'referenceCorrelationMatrix'
        }

        self._assets = assets
        self._assets_correlation_matrix = assets_correlation_matrix
        self._distance_metric = distance_metric
        self._reference_correlation_matrix = reference_correlation_matrix

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsCorrelationMatrixDistancePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_correlation_matrix_distance_post_request of this AssetsCorrelationMatrixDistancePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this AssetsCorrelationMatrixDistancePostRequest.


        :return: The assets of this AssetsCorrelationMatrixDistancePostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetsCorrelationMatrixDistancePostRequest.


        :param assets: The assets of this AssetsCorrelationMatrixDistancePostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and assets < 2:
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `2`")

        self._assets = assets

    @property
    def assets_correlation_matrix(self):
        """Gets the assets_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.

        assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        :return: The assets_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        :rtype: List[List[float]]
        """
        return self._assets_correlation_matrix

    @assets_correlation_matrix.setter
    def assets_correlation_matrix(self, assets_correlation_matrix):
        """Sets the assets_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.

        assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        :param assets_correlation_matrix: The assets_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        :type assets_correlation_matrix: List[List[float]]
        """
        if assets_correlation_matrix is None:
            raise ValueError("Invalid value for `assets_correlation_matrix`, must not be `None`")
        if assets_correlation_matrix is not None and len(assets_correlation_matrix) < 2:
            raise ValueError("Invalid value for `assets_correlation_matrix`, number of items must be greater than or equal to `2`")

        self._assets_correlation_matrix = assets_correlation_matrix

    @property
    def distance_metric(self):
        """Gets the distance_metric of this AssetsCorrelationMatrixDistancePostRequest.

        The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix

        :return: The distance_metric of this AssetsCorrelationMatrixDistancePostRequest.
        :rtype: str
        """
        return self._distance_metric

    @distance_metric.setter
    def distance_metric(self, distance_metric):
        """Sets the distance_metric of this AssetsCorrelationMatrixDistancePostRequest.

        The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix

        :param distance_metric: The distance_metric of this AssetsCorrelationMatrixDistancePostRequest.
        :type distance_metric: str
        """
        allowed_values = ["euclidean", "correlationMatrix", "bures"]  # noqa: E501
        if distance_metric not in allowed_values:
            raise ValueError(
                "Invalid value for `distance_metric` ({0}), must be one of {1}"
                .format(distance_metric, allowed_values)
            )

        self._distance_metric = distance_metric

    @property
    def reference_correlation_matrix(self):
        """Gets the reference_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.

        referenceCorrelationMatrix[i][j] is the reference correlation between the asset i and the asset j

        :return: The reference_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        :rtype: List[List[float]]
        """
        return self._reference_correlation_matrix

    @reference_correlation_matrix.setter
    def reference_correlation_matrix(self, reference_correlation_matrix):
        """Sets the reference_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.

        referenceCorrelationMatrix[i][j] is the reference correlation between the asset i and the asset j

        :param reference_correlation_matrix: The reference_correlation_matrix of this AssetsCorrelationMatrixDistancePostRequest.
        :type reference_correlation_matrix: List[List[float]]
        """
        if reference_correlation_matrix is None:
            raise ValueError("Invalid value for `reference_correlation_matrix`, must not be `None`")
        if reference_correlation_matrix is not None and len(reference_correlation_matrix) < 2:
            raise ValueError("Invalid value for `reference_correlation_matrix`, number of items must be greater than or equal to `2`")

        self._reference_correlation_matrix = reference_correlation_matrix
