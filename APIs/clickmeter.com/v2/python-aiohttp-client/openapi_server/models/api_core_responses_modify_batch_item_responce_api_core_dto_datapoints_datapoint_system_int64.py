# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.click_meter_infrastructure_validation_validation_failure import ClickMeterInfrastructureValidationValidationFailure
from openapi_server import util


class ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_data: ApiCoreDtoDatapointsDatapoint=None, errors: List[ClickMeterInfrastructureValidationValidationFailure]=None, result: ApiCoreResponsesEntityUriSystemInt64=None, status: str=None):
        """ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 - a model defined in OpenAPI

        :param entity_data: The entity_data of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :param errors: The errors of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :param result: The result of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :param status: The status of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        """
        self.openapi_types = {
            'entity_data': ApiCoreDtoDatapointsDatapoint,
            'errors': List[ClickMeterInfrastructureValidationValidationFailure],
            'result': ApiCoreResponsesEntityUriSystemInt64,
            'status': str
        }

        self.attribute_map = {
            'entity_data': 'entityData',
            'errors': 'errors',
            'result': 'result',
            'status': 'status'
        }

        self._entity_data = entity_data
        self._errors = errors
        self._result = result
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Responses.ModifyBatchItemResponce_Api.Core.Dto.Datapoints.Datapoint_System.Int64_ of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_data(self):
        """Gets the entity_data of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :return: The entity_data of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :rtype: ApiCoreDtoDatapointsDatapoint
        """
        return self._entity_data

    @entity_data.setter
    def entity_data(self, entity_data):
        """Sets the entity_data of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :param entity_data: The entity_data of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :type entity_data: ApiCoreDtoDatapointsDatapoint
        """

        self._entity_data = entity_data

    @property
    def errors(self):
        """Gets the errors of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :return: The errors of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :rtype: List[ClickMeterInfrastructureValidationValidationFailure]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :param errors: The errors of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :type errors: List[ClickMeterInfrastructureValidationValidationFailure]
        """

        self._errors = errors

    @property
    def result(self):
        """Gets the result of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :return: The result of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :rtype: ApiCoreResponsesEntityUriSystemInt64
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :param result: The result of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :type result: ApiCoreResponsesEntityUriSystemInt64
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :return: The status of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.


        :param status: The status of this ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.
        :type status: str
        """

        self._status = status
