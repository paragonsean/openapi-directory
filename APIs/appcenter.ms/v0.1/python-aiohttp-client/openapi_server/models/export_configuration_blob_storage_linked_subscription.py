# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ExportConfigurationBlobStorageLinkedSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subscription_id: str=None, blob_path_format_kind: str=None, backfill: bool=None, export_entities: List[str]=None, resource_group: str=None, resource_name: str=None, type: str=None):
        """ExportConfigurationBlobStorageLinkedSubscription - a model defined in OpenAPI

        :param subscription_id: The subscription_id of this ExportConfigurationBlobStorageLinkedSubscription.
        :param blob_path_format_kind: The blob_path_format_kind of this ExportConfigurationBlobStorageLinkedSubscription.
        :param backfill: The backfill of this ExportConfigurationBlobStorageLinkedSubscription.
        :param export_entities: The export_entities of this ExportConfigurationBlobStorageLinkedSubscription.
        :param resource_group: The resource_group of this ExportConfigurationBlobStorageLinkedSubscription.
        :param resource_name: The resource_name of this ExportConfigurationBlobStorageLinkedSubscription.
        :param type: The type of this ExportConfigurationBlobStorageLinkedSubscription.
        """
        self.openapi_types = {
            'subscription_id': str,
            'blob_path_format_kind': str,
            'backfill': bool,
            'export_entities': List[str],
            'resource_group': str,
            'resource_name': str,
            'type': str
        }

        self.attribute_map = {
            'subscription_id': 'subscription_id',
            'blob_path_format_kind': 'blob_path_format_kind',
            'backfill': 'backfill',
            'export_entities': 'export_entities',
            'resource_group': 'resource_group',
            'resource_name': 'resource_name',
            'type': 'type'
        }

        self._subscription_id = subscription_id
        self._blob_path_format_kind = blob_path_format_kind
        self._backfill = backfill
        self._export_entities = export_entities
        self._resource_group = resource_group
        self._resource_name = resource_name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExportConfigurationBlobStorageLinkedSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExportConfigurationBlobStorageLinkedSubscription of this ExportConfigurationBlobStorageLinkedSubscription.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ExportConfigurationBlobStorageLinkedSubscription.

        Id of customer subscription linked in App Center

        :return: The subscription_id of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ExportConfigurationBlobStorageLinkedSubscription.

        Id of customer subscription linked in App Center

        :param subscription_id: The subscription_id of this ExportConfigurationBlobStorageLinkedSubscription.
        :type subscription_id: str
        """
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")

        self._subscription_id = subscription_id

    @property
    def blob_path_format_kind(self):
        """Gets the blob_path_format_kind of this ExportConfigurationBlobStorageLinkedSubscription.

        The path to the blob when enum set to 'WithoutAppId' is 'year/month/day/hour/minute' and when set to 'WithAppId' is 'appId/year/month/day/hour/minute'

        :return: The blob_path_format_kind of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: str
        """
        return self._blob_path_format_kind

    @blob_path_format_kind.setter
    def blob_path_format_kind(self, blob_path_format_kind):
        """Sets the blob_path_format_kind of this ExportConfigurationBlobStorageLinkedSubscription.

        The path to the blob when enum set to 'WithoutAppId' is 'year/month/day/hour/minute' and when set to 'WithAppId' is 'appId/year/month/day/hour/minute'

        :param blob_path_format_kind: The blob_path_format_kind of this ExportConfigurationBlobStorageLinkedSubscription.
        :type blob_path_format_kind: str
        """
        allowed_values = ["WithoutAppId", "WithAppId"]  # noqa: E501
        if blob_path_format_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `blob_path_format_kind` ({0}), must be one of {1}"
                .format(blob_path_format_kind, allowed_values)
            )

        self._blob_path_format_kind = blob_path_format_kind

    @property
    def backfill(self):
        """Gets the backfill of this ExportConfigurationBlobStorageLinkedSubscription.

        Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation.

        :return: The backfill of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: bool
        """
        return self._backfill

    @backfill.setter
    def backfill(self, backfill):
        """Sets the backfill of this ExportConfigurationBlobStorageLinkedSubscription.

        Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation.

        :param backfill: The backfill of this ExportConfigurationBlobStorageLinkedSubscription.
        :type backfill: bool
        """

        self._backfill = backfill

    @property
    def export_entities(self):
        """Gets the export_entities of this ExportConfigurationBlobStorageLinkedSubscription.


        :return: The export_entities of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: List[str]
        """
        return self._export_entities

    @export_entities.setter
    def export_entities(self, export_entities):
        """Sets the export_entities of this ExportConfigurationBlobStorageLinkedSubscription.


        :param export_entities: The export_entities of this ExportConfigurationBlobStorageLinkedSubscription.
        :type export_entities: List[str]
        """
        allowed_values = ["crashes", "errors", "attachments", "no_logs"]  # noqa: E501
        if not set(export_entities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `export_entities` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(export_entities) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._export_entities = export_entities

    @property
    def resource_group(self):
        """Gets the resource_group of this ExportConfigurationBlobStorageLinkedSubscription.

        The resource group name on azure

        :return: The resource_group of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this ExportConfigurationBlobStorageLinkedSubscription.

        The resource group name on azure

        :param resource_group: The resource_group of this ExportConfigurationBlobStorageLinkedSubscription.
        :type resource_group: str
        """

        self._resource_group = resource_group

    @property
    def resource_name(self):
        """Gets the resource_name of this ExportConfigurationBlobStorageLinkedSubscription.

        The resource name on azure

        :return: The resource_name of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ExportConfigurationBlobStorageLinkedSubscription.

        The resource name on azure

        :param resource_name: The resource_name of this ExportConfigurationBlobStorageLinkedSubscription.
        :type resource_name: str
        """

        self._resource_name = resource_name

    @property
    def type(self):
        """Gets the type of this ExportConfigurationBlobStorageLinkedSubscription.

        Type of export configuration

        :return: The type of this ExportConfigurationBlobStorageLinkedSubscription.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportConfigurationBlobStorageLinkedSubscription.

        Type of export configuration

        :param type: The type of this ExportConfigurationBlobStorageLinkedSubscription.
        :type type: str
        """
        allowed_values = ["blob_storage_connection_string", "application_insights_instrumentation_key", "blob_storage_linked_subscription", "application_insights_linked_subscription"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
