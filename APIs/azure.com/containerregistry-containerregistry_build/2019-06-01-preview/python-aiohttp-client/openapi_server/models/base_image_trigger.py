# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BaseImageTrigger(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_image_trigger_type: str=None, name: str=None, status: str='Enabled', update_trigger_endpoint: str=None, update_trigger_payload_type: str=None):
        """BaseImageTrigger - a model defined in OpenAPI

        :param base_image_trigger_type: The base_image_trigger_type of this BaseImageTrigger.
        :param name: The name of this BaseImageTrigger.
        :param status: The status of this BaseImageTrigger.
        :param update_trigger_endpoint: The update_trigger_endpoint of this BaseImageTrigger.
        :param update_trigger_payload_type: The update_trigger_payload_type of this BaseImageTrigger.
        """
        self.openapi_types = {
            'base_image_trigger_type': str,
            'name': str,
            'status': str,
            'update_trigger_endpoint': str,
            'update_trigger_payload_type': str
        }

        self.attribute_map = {
            'base_image_trigger_type': 'baseImageTriggerType',
            'name': 'name',
            'status': 'status',
            'update_trigger_endpoint': 'updateTriggerEndpoint',
            'update_trigger_payload_type': 'updateTriggerPayloadType'
        }

        self._base_image_trigger_type = base_image_trigger_type
        self._name = name
        self._status = status
        self._update_trigger_endpoint = update_trigger_endpoint
        self._update_trigger_payload_type = update_trigger_payload_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BaseImageTrigger':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BaseImageTrigger of this BaseImageTrigger.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_image_trigger_type(self):
        """Gets the base_image_trigger_type of this BaseImageTrigger.

        The type of the auto trigger for base image dependency updates.

        :return: The base_image_trigger_type of this BaseImageTrigger.
        :rtype: str
        """
        return self._base_image_trigger_type

    @base_image_trigger_type.setter
    def base_image_trigger_type(self, base_image_trigger_type):
        """Sets the base_image_trigger_type of this BaseImageTrigger.

        The type of the auto trigger for base image dependency updates.

        :param base_image_trigger_type: The base_image_trigger_type of this BaseImageTrigger.
        :type base_image_trigger_type: str
        """
        allowed_values = ["All", "Runtime"]  # noqa: E501
        if base_image_trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `base_image_trigger_type` ({0}), must be one of {1}"
                .format(base_image_trigger_type, allowed_values)
            )

        self._base_image_trigger_type = base_image_trigger_type

    @property
    def name(self):
        """Gets the name of this BaseImageTrigger.

        The name of the trigger.

        :return: The name of this BaseImageTrigger.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseImageTrigger.

        The name of the trigger.

        :param name: The name of this BaseImageTrigger.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self):
        """Gets the status of this BaseImageTrigger.

        The current status of trigger.

        :return: The status of this BaseImageTrigger.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseImageTrigger.

        The current status of trigger.

        :param status: The status of this BaseImageTrigger.
        :type status: str
        """
        allowed_values = ["Disabled", "Enabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def update_trigger_endpoint(self):
        """Gets the update_trigger_endpoint of this BaseImageTrigger.

        The endpoint URL for receiving update triggers.

        :return: The update_trigger_endpoint of this BaseImageTrigger.
        :rtype: str
        """
        return self._update_trigger_endpoint

    @update_trigger_endpoint.setter
    def update_trigger_endpoint(self, update_trigger_endpoint):
        """Sets the update_trigger_endpoint of this BaseImageTrigger.

        The endpoint URL for receiving update triggers.

        :param update_trigger_endpoint: The update_trigger_endpoint of this BaseImageTrigger.
        :type update_trigger_endpoint: str
        """

        self._update_trigger_endpoint = update_trigger_endpoint

    @property
    def update_trigger_payload_type(self):
        """Gets the update_trigger_payload_type of this BaseImageTrigger.

        Type of Payload body for Base image update triggers.

        :return: The update_trigger_payload_type of this BaseImageTrigger.
        :rtype: str
        """
        return self._update_trigger_payload_type

    @update_trigger_payload_type.setter
    def update_trigger_payload_type(self, update_trigger_payload_type):
        """Sets the update_trigger_payload_type of this BaseImageTrigger.

        Type of Payload body for Base image update triggers.

        :param update_trigger_payload_type: The update_trigger_payload_type of this BaseImageTrigger.
        :type update_trigger_payload_type: str
        """
        allowed_values = ["Default", "Token"]  # noqa: E501
        if update_trigger_payload_type not in allowed_values:
            raise ValueError(
                "Invalid value for `update_trigger_payload_type` ({0}), must be one of {1}"
                .format(update_trigger_payload_type, allowed_values)
            )

        self._update_trigger_payload_type = update_trigger_payload_type
