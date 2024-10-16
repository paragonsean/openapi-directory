# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_fact_finder_snapshot_domain_object import IFactFinderSnapshotDomainObject
from openapi_server import util


class FactFinderSnapshotWithIdModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, fact_finder_data: IFactFinderSnapshotDomainObject=None, fact_finder_id: int=None, fact_finder_status: str=None, snapshot_id: int=None):
        """FactFinderSnapshotWithIdModel - a model defined in OpenAPI

        :param created: The created of this FactFinderSnapshotWithIdModel.
        :param fact_finder_data: The fact_finder_data of this FactFinderSnapshotWithIdModel.
        :param fact_finder_id: The fact_finder_id of this FactFinderSnapshotWithIdModel.
        :param fact_finder_status: The fact_finder_status of this FactFinderSnapshotWithIdModel.
        :param snapshot_id: The snapshot_id of this FactFinderSnapshotWithIdModel.
        """
        self.openapi_types = {
            'created': datetime,
            'fact_finder_data': IFactFinderSnapshotDomainObject,
            'fact_finder_id': int,
            'fact_finder_status': str,
            'snapshot_id': int
        }

        self.attribute_map = {
            'created': 'created',
            'fact_finder_data': 'factFinderData',
            'fact_finder_id': 'factFinderId',
            'fact_finder_status': 'factFinderStatus',
            'snapshot_id': 'snapshotId'
        }

        self._created = created
        self._fact_finder_data = fact_finder_data
        self._fact_finder_id = fact_finder_id
        self._fact_finder_status = fact_finder_status
        self._snapshot_id = snapshot_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FactFinderSnapshotWithIdModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FactFinderSnapshotWithIdModel of this FactFinderSnapshotWithIdModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this FactFinderSnapshotWithIdModel.


        :return: The created of this FactFinderSnapshotWithIdModel.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FactFinderSnapshotWithIdModel.


        :param created: The created of this FactFinderSnapshotWithIdModel.
        :type created: datetime
        """

        self._created = created

    @property
    def fact_finder_data(self):
        """Gets the fact_finder_data of this FactFinderSnapshotWithIdModel.


        :return: The fact_finder_data of this FactFinderSnapshotWithIdModel.
        :rtype: IFactFinderSnapshotDomainObject
        """
        return self._fact_finder_data

    @fact_finder_data.setter
    def fact_finder_data(self, fact_finder_data):
        """Sets the fact_finder_data of this FactFinderSnapshotWithIdModel.


        :param fact_finder_data: The fact_finder_data of this FactFinderSnapshotWithIdModel.
        :type fact_finder_data: IFactFinderSnapshotDomainObject
        """

        self._fact_finder_data = fact_finder_data

    @property
    def fact_finder_id(self):
        """Gets the fact_finder_id of this FactFinderSnapshotWithIdModel.


        :return: The fact_finder_id of this FactFinderSnapshotWithIdModel.
        :rtype: int
        """
        return self._fact_finder_id

    @fact_finder_id.setter
    def fact_finder_id(self, fact_finder_id):
        """Sets the fact_finder_id of this FactFinderSnapshotWithIdModel.


        :param fact_finder_id: The fact_finder_id of this FactFinderSnapshotWithIdModel.
        :type fact_finder_id: int
        """

        self._fact_finder_id = fact_finder_id

    @property
    def fact_finder_status(self):
        """Gets the fact_finder_status of this FactFinderSnapshotWithIdModel.


        :return: The fact_finder_status of this FactFinderSnapshotWithIdModel.
        :rtype: str
        """
        return self._fact_finder_status

    @fact_finder_status.setter
    def fact_finder_status(self, fact_finder_status):
        """Sets the fact_finder_status of this FactFinderSnapshotWithIdModel.


        :param fact_finder_status: The fact_finder_status of this FactFinderSnapshotWithIdModel.
        :type fact_finder_status: str
        """
        allowed_values = ["New", "InProgress", "ClientSubmitted", "AdvisorAccepted", "Canceled", "Draft", "Deleted"]  # noqa: E501
        if fact_finder_status not in allowed_values:
            raise ValueError(
                "Invalid value for `fact_finder_status` ({0}), must be one of {1}"
                .format(fact_finder_status, allowed_values)
            )

        self._fact_finder_status = fact_finder_status

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this FactFinderSnapshotWithIdModel.


        :return: The snapshot_id of this FactFinderSnapshotWithIdModel.
        :rtype: int
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this FactFinderSnapshotWithIdModel.


        :param snapshot_id: The snapshot_id of this FactFinderSnapshotWithIdModel.
        :type snapshot_id: int
        """

        self._snapshot_id = snapshot_id
