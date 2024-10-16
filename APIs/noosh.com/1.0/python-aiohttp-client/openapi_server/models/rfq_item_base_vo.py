# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.ergo_spec_simple_vo import ErgoSpecSimpleVO
from openapi_server import util


class RfqItemBaseVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_id: int=None, rfq_item_id: int=None, spec: ErgoSpecSimpleVO=None):
        """RfqItemBaseVO - a model defined in OpenAPI

        :param job_id: The job_id of this RfqItemBaseVO.
        :param rfq_item_id: The rfq_item_id of this RfqItemBaseVO.
        :param spec: The spec of this RfqItemBaseVO.
        """
        self.openapi_types = {
            'job_id': int,
            'rfq_item_id': int,
            'spec': ErgoSpecSimpleVO
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'rfq_item_id': 'rfq_item_id',
            'spec': 'spec'
        }

        self._job_id = job_id
        self._rfq_item_id = rfq_item_id
        self._spec = spec

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RfqItemBaseVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RfqItemBaseVO of this RfqItemBaseVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self):
        """Gets the job_id of this RfqItemBaseVO.

        

        :return: The job_id of this RfqItemBaseVO.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RfqItemBaseVO.

        

        :param job_id: The job_id of this RfqItemBaseVO.
        :type job_id: int
        """

        self._job_id = job_id

    @property
    def rfq_item_id(self):
        """Gets the rfq_item_id of this RfqItemBaseVO.

        

        :return: The rfq_item_id of this RfqItemBaseVO.
        :rtype: int
        """
        return self._rfq_item_id

    @rfq_item_id.setter
    def rfq_item_id(self, rfq_item_id):
        """Sets the rfq_item_id of this RfqItemBaseVO.

        

        :param rfq_item_id: The rfq_item_id of this RfqItemBaseVO.
        :type rfq_item_id: int
        """

        self._rfq_item_id = rfq_item_id

    @property
    def spec(self):
        """Gets the spec of this RfqItemBaseVO.


        :return: The spec of this RfqItemBaseVO.
        :rtype: ErgoSpecSimpleVO
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this RfqItemBaseVO.


        :param spec: The spec of this RfqItemBaseVO.
        :type spec: ErgoSpecSimpleVO
        """

        self._spec = spec
