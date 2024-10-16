# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.anonymization_profile import AnonymizationProfile
from openapi_server import util


class OutgoingTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, box_id: int=None, box_name: str=None, id: int=None, profile: AnonymizationProfile=None, sent_image_count: int=None, status: str=None, total_image_count: int=None, updated: int=None):
        """OutgoingTransaction - a model defined in OpenAPI

        :param box_id: The box_id of this OutgoingTransaction.
        :param box_name: The box_name of this OutgoingTransaction.
        :param id: The id of this OutgoingTransaction.
        :param profile: The profile of this OutgoingTransaction.
        :param sent_image_count: The sent_image_count of this OutgoingTransaction.
        :param status: The status of this OutgoingTransaction.
        :param total_image_count: The total_image_count of this OutgoingTransaction.
        :param updated: The updated of this OutgoingTransaction.
        """
        self.openapi_types = {
            'box_id': int,
            'box_name': str,
            'id': int,
            'profile': AnonymizationProfile,
            'sent_image_count': int,
            'status': str,
            'total_image_count': int,
            'updated': int
        }

        self.attribute_map = {
            'box_id': 'boxId',
            'box_name': 'boxName',
            'id': 'id',
            'profile': 'profile',
            'sent_image_count': 'sentImageCount',
            'status': 'status',
            'total_image_count': 'totalImageCount',
            'updated': 'updated'
        }

        self._box_id = box_id
        self._box_name = box_name
        self._id = id
        self._profile = profile
        self._sent_image_count = sent_image_count
        self._status = status
        self._total_image_count = total_image_count
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutgoingTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The outgoingTransaction of this OutgoingTransaction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def box_id(self):
        """Gets the box_id of this OutgoingTransaction.


        :return: The box_id of this OutgoingTransaction.
        :rtype: int
        """
        return self._box_id

    @box_id.setter
    def box_id(self, box_id):
        """Sets the box_id of this OutgoingTransaction.


        :param box_id: The box_id of this OutgoingTransaction.
        :type box_id: int
        """

        self._box_id = box_id

    @property
    def box_name(self):
        """Gets the box_name of this OutgoingTransaction.


        :return: The box_name of this OutgoingTransaction.
        :rtype: str
        """
        return self._box_name

    @box_name.setter
    def box_name(self, box_name):
        """Sets the box_name of this OutgoingTransaction.


        :param box_name: The box_name of this OutgoingTransaction.
        :type box_name: str
        """

        self._box_name = box_name

    @property
    def id(self):
        """Gets the id of this OutgoingTransaction.


        :return: The id of this OutgoingTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OutgoingTransaction.


        :param id: The id of this OutgoingTransaction.
        :type id: int
        """

        self._id = id

    @property
    def profile(self):
        """Gets the profile of this OutgoingTransaction.


        :return: The profile of this OutgoingTransaction.
        :rtype: AnonymizationProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this OutgoingTransaction.


        :param profile: The profile of this OutgoingTransaction.
        :type profile: AnonymizationProfile
        """

        self._profile = profile

    @property
    def sent_image_count(self):
        """Gets the sent_image_count of this OutgoingTransaction.


        :return: The sent_image_count of this OutgoingTransaction.
        :rtype: int
        """
        return self._sent_image_count

    @sent_image_count.setter
    def sent_image_count(self, sent_image_count):
        """Sets the sent_image_count of this OutgoingTransaction.


        :param sent_image_count: The sent_image_count of this OutgoingTransaction.
        :type sent_image_count: int
        """

        self._sent_image_count = sent_image_count

    @property
    def status(self):
        """Gets the status of this OutgoingTransaction.


        :return: The status of this OutgoingTransaction.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OutgoingTransaction.


        :param status: The status of this OutgoingTransaction.
        :type status: str
        """

        self._status = status

    @property
    def total_image_count(self):
        """Gets the total_image_count of this OutgoingTransaction.


        :return: The total_image_count of this OutgoingTransaction.
        :rtype: int
        """
        return self._total_image_count

    @total_image_count.setter
    def total_image_count(self, total_image_count):
        """Sets the total_image_count of this OutgoingTransaction.


        :param total_image_count: The total_image_count of this OutgoingTransaction.
        :type total_image_count: int
        """

        self._total_image_count = total_image_count

    @property
    def updated(self):
        """Gets the updated of this OutgoingTransaction.


        :return: The updated of this OutgoingTransaction.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this OutgoingTransaction.


        :param updated: The updated of this OutgoingTransaction.
        :type updated: int
        """

        self._updated = updated
