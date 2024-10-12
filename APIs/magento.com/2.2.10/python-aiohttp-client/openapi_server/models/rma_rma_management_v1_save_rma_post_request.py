# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.rma_data_rma_interface import RmaDataRmaInterface
from openapi_server import util


class RmaRmaManagementV1SaveRmaPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rma_data_object: RmaDataRmaInterface=None):
        """RmaRmaManagementV1SaveRmaPostRequest - a model defined in OpenAPI

        :param rma_data_object: The rma_data_object of this RmaRmaManagementV1SaveRmaPostRequest.
        """
        self.openapi_types = {
            'rma_data_object': RmaDataRmaInterface
        }

        self.attribute_map = {
            'rma_data_object': 'rmaDataObject'
        }

        self._rma_data_object = rma_data_object

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RmaRmaManagementV1SaveRmaPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The rmaRmaManagementV1SaveRmaPost_request of this RmaRmaManagementV1SaveRmaPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rma_data_object(self):
        """Gets the rma_data_object of this RmaRmaManagementV1SaveRmaPostRequest.


        :return: The rma_data_object of this RmaRmaManagementV1SaveRmaPostRequest.
        :rtype: RmaDataRmaInterface
        """
        return self._rma_data_object

    @rma_data_object.setter
    def rma_data_object(self, rma_data_object):
        """Sets the rma_data_object of this RmaRmaManagementV1SaveRmaPostRequest.


        :param rma_data_object: The rma_data_object of this RmaRmaManagementV1SaveRmaPostRequest.
        :type rma_data_object: RmaDataRmaInterface
        """
        if rma_data_object is None:
            raise ValueError("Invalid value for `rma_data_object`, must not be `None`")

        self._rma_data_object = rma_data_object
