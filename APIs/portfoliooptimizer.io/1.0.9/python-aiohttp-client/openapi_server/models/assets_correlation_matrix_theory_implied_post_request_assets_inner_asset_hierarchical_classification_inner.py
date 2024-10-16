# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInnerAssetHierarchicalClassificationInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):
        """AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInnerAssetHierarchicalClassificationInner - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInnerAssetHierarchicalClassificationInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_correlation_matrix_theory_implied_post_request_assets_inner_assetHierarchicalClassification_inner of this AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInnerAssetHierarchicalClassificationInner.
        """
        return util.deserialize_model(dikt, cls)
