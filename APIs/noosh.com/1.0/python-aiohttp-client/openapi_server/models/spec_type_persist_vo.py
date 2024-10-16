# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SpecTypePersistVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, prd_type_labels: List[str]=None, spec_type_id: int=None):
        """SpecTypePersistVO - a model defined in OpenAPI

        :param prd_type_labels: The prd_type_labels of this SpecTypePersistVO.
        :param spec_type_id: The spec_type_id of this SpecTypePersistVO.
        """
        self.openapi_types = {
            'prd_type_labels': List[str],
            'spec_type_id': int
        }

        self.attribute_map = {
            'prd_type_labels': 'prdType_labels',
            'spec_type_id': 'spec_type_id'
        }

        self._prd_type_labels = prd_type_labels
        self._spec_type_id = spec_type_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SpecTypePersistVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SpecTypePersistVO of this SpecTypePersistVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def prd_type_labels(self):
        """Gets the prd_type_labels of this SpecTypePersistVO.

        

        :return: The prd_type_labels of this SpecTypePersistVO.
        :rtype: List[str]
        """
        return self._prd_type_labels

    @prd_type_labels.setter
    def prd_type_labels(self, prd_type_labels):
        """Sets the prd_type_labels of this SpecTypePersistVO.

        

        :param prd_type_labels: The prd_type_labels of this SpecTypePersistVO.
        :type prd_type_labels: List[str]
        """

        self._prd_type_labels = prd_type_labels

    @property
    def spec_type_id(self):
        """Gets the spec_type_id of this SpecTypePersistVO.

        

        :return: The spec_type_id of this SpecTypePersistVO.
        :rtype: int
        """
        return self._spec_type_id

    @spec_type_id.setter
    def spec_type_id(self, spec_type_id):
        """Sets the spec_type_id of this SpecTypePersistVO.

        

        :param spec_type_id: The spec_type_id of this SpecTypePersistVO.
        :type spec_type_id: int
        """

        self._spec_type_id = spec_type_id
