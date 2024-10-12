# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JobStage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, detail: str=None, error_code: str=None, message: str=None, stage_status: str=None):
        """JobStage - a model defined in OpenAPI

        :param detail: The detail of this JobStage.
        :param error_code: The error_code of this JobStage.
        :param message: The message of this JobStage.
        :param stage_status: The stage_status of this JobStage.
        """
        self.openapi_types = {
            'detail': str,
            'error_code': str,
            'message': str,
            'stage_status': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'error_code': 'errorCode',
            'message': 'message',
            'stage_status': 'stageStatus'
        }

        self._detail = detail
        self._error_code = error_code
        self._message = message
        self._stage_status = stage_status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JobStage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JobStage of this JobStage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self):
        """Gets the detail of this JobStage.

        The details of the stage.

        :return: The detail of this JobStage.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this JobStage.

        The details of the stage.

        :param detail: The detail of this JobStage.
        :type detail: str
        """

        self._detail = detail

    @property
    def error_code(self):
        """Gets the error_code of this JobStage.

        The error code of the stage if any.

        :return: The error_code of this JobStage.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this JobStage.

        The error code of the stage if any.

        :param error_code: The error_code of this JobStage.
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this JobStage.

        The message of the job stage.

        :return: The message of this JobStage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobStage.

        The message of the job stage.

        :param message: The message of this JobStage.
        :type message: str
        """

        self._message = message

    @property
    def stage_status(self):
        """Gets the stage_status of this JobStage.

        The stage status.

        :return: The stage_status of this JobStage.
        :rtype: str
        """
        return self._stage_status

    @stage_status.setter
    def stage_status(self, stage_status):
        """Sets the stage_status of this JobStage.

        The stage status.

        :param stage_status: The stage_status of this JobStage.
        :type stage_status: str
        """
        allowed_values = ["Running", "Succeeded", "Failed", "Canceled"]  # noqa: E501
        if stage_status not in allowed_values:
            raise ValueError(
                "Invalid value for `stage_status` ({0}), must be one of {1}"
                .format(stage_status, allowed_values)
            )

        self._stage_status = stage_status
