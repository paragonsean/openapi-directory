# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_firmware_upgrades_rollback200_response_reasons_inner import CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
from openapi_server.models.create_network_firmware_upgrades_rollback200_response_to_version import CreateNetworkFirmwareUpgradesRollback200ResponseToVersion
from openapi_server import util


class CreateNetworkFirmwareUpgradesRollback200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, product: str=None, reasons: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]=None, status: str=None, time: datetime=None, to_version: CreateNetworkFirmwareUpgradesRollback200ResponseToVersion=None, upgrade_batch_id: str=None):
        """CreateNetworkFirmwareUpgradesRollback200Response - a model defined in OpenAPI

        :param product: The product of this CreateNetworkFirmwareUpgradesRollback200Response.
        :param reasons: The reasons of this CreateNetworkFirmwareUpgradesRollback200Response.
        :param status: The status of this CreateNetworkFirmwareUpgradesRollback200Response.
        :param time: The time of this CreateNetworkFirmwareUpgradesRollback200Response.
        :param to_version: The to_version of this CreateNetworkFirmwareUpgradesRollback200Response.
        :param upgrade_batch_id: The upgrade_batch_id of this CreateNetworkFirmwareUpgradesRollback200Response.
        """
        self.openapi_types = {
            'product': str,
            'reasons': List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner],
            'status': str,
            'time': datetime,
            'to_version': CreateNetworkFirmwareUpgradesRollback200ResponseToVersion,
            'upgrade_batch_id': str
        }

        self.attribute_map = {
            'product': 'product',
            'reasons': 'reasons',
            'status': 'status',
            'time': 'time',
            'to_version': 'toVersion',
            'upgrade_batch_id': 'upgradeBatchId'
        }

        self._product = product
        self._reasons = reasons
        self._status = status
        self._time = time
        self._to_version = to_version
        self._upgrade_batch_id = upgrade_batch_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkFirmwareUpgradesRollback200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkFirmwareUpgradesRollback_200_response of this CreateNetworkFirmwareUpgradesRollback200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product(self):
        """Gets the product of this CreateNetworkFirmwareUpgradesRollback200Response.

        Product type to rollback (if the network is a combined network)

        :return: The product of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CreateNetworkFirmwareUpgradesRollback200Response.

        Product type to rollback (if the network is a combined network)

        :param product: The product of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type product: str
        """
        allowed_values = ["appliance", "camera", "cellularGateway", "switch", "wireless"]  # noqa: E501
        if product not in allowed_values:
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"
                .format(product, allowed_values)
            )

        self._product = product

    @property
    def reasons(self):
        """Gets the reasons of this CreateNetworkFirmwareUpgradesRollback200Response.

        Reasons for the rollback

        :return: The reasons of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this CreateNetworkFirmwareUpgradesRollback200Response.

        Reasons for the rollback

        :param reasons: The reasons of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type reasons: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]
        """

        self._reasons = reasons

    @property
    def status(self):
        """Gets the status of this CreateNetworkFirmwareUpgradesRollback200Response.

        Status of the rollback

        :return: The status of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateNetworkFirmwareUpgradesRollback200Response.

        Status of the rollback

        :param status: The status of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type status: str
        """
        allowed_values = ["canceled", "completed", "in_progress", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def time(self):
        """Gets the time of this CreateNetworkFirmwareUpgradesRollback200Response.

        Scheduled time for the rollback

        :return: The time of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CreateNetworkFirmwareUpgradesRollback200Response.

        Scheduled time for the rollback

        :param time: The time of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type time: datetime
        """

        self._time = time

    @property
    def to_version(self):
        """Gets the to_version of this CreateNetworkFirmwareUpgradesRollback200Response.


        :return: The to_version of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: CreateNetworkFirmwareUpgradesRollback200ResponseToVersion
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        """Sets the to_version of this CreateNetworkFirmwareUpgradesRollback200Response.


        :param to_version: The to_version of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type to_version: CreateNetworkFirmwareUpgradesRollback200ResponseToVersion
        """

        self._to_version = to_version

    @property
    def upgrade_batch_id(self):
        """Gets the upgrade_batch_id of this CreateNetworkFirmwareUpgradesRollback200Response.

        Batch ID of the firmware rollback

        :return: The upgrade_batch_id of this CreateNetworkFirmwareUpgradesRollback200Response.
        :rtype: str
        """
        return self._upgrade_batch_id

    @upgrade_batch_id.setter
    def upgrade_batch_id(self, upgrade_batch_id):
        """Sets the upgrade_batch_id of this CreateNetworkFirmwareUpgradesRollback200Response.

        Batch ID of the firmware rollback

        :param upgrade_batch_id: The upgrade_batch_id of this CreateNetworkFirmwareUpgradesRollback200Response.
        :type upgrade_batch_id: str
        """

        self._upgrade_batch_id = upgrade_batch_id
