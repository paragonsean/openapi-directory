# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.group_message import GroupMessage
from openapi_server import util


class EndpointPostGroupsMessagesMetadataFiltersDataInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, matched_metadata: Dict[str, List[str]]=None, message: GroupMessage=None):
        """EndpointPostGroupsMessagesMetadataFiltersDataInner - a model defined in OpenAPI

        :param matched_metadata: The matched_metadata of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        :param message: The message of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        """
        self.openapi_types = {
            'matched_metadata': Dict[str, List[str]],
            'message': GroupMessage
        }

        self.attribute_map = {
            'matched_metadata': 'matched_metadata',
            'message': 'message'
        }

        self._matched_metadata = matched_metadata
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPostGroupsMessagesMetadataFiltersDataInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint_post_groups_messages_metadata_filters_data_inner of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def matched_metadata(self):
        """Gets the matched_metadata of this EndpointPostGroupsMessagesMetadataFiltersDataInner.


        :return: The matched_metadata of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        :rtype: Dict[str, List[str]]
        """
        return self._matched_metadata

    @matched_metadata.setter
    def matched_metadata(self, matched_metadata):
        """Sets the matched_metadata of this EndpointPostGroupsMessagesMetadataFiltersDataInner.


        :param matched_metadata: The matched_metadata of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        :type matched_metadata: Dict[str, List[str]]
        """

        self._matched_metadata = matched_metadata

    @property
    def message(self):
        """Gets the message of this EndpointPostGroupsMessagesMetadataFiltersDataInner.


        :return: The message of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        :rtype: GroupMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EndpointPostGroupsMessagesMetadataFiltersDataInner.


        :param message: The message of this EndpointPostGroupsMessagesMetadataFiltersDataInner.
        :type message: GroupMessage
        """

        self._message = message
