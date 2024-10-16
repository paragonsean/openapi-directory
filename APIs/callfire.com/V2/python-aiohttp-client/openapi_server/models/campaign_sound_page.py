# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.campaign_sound import CampaignSound
from openapi_server import util


class CampaignSoundPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[CampaignSound]=None, limit: int=None, offset: int=None, total_count: int=None):
        """CampaignSoundPage - a model defined in OpenAPI

        :param items: The items of this CampaignSoundPage.
        :param limit: The limit of this CampaignSoundPage.
        :param offset: The offset of this CampaignSoundPage.
        :param total_count: The total_count of this CampaignSoundPage.
        """
        self.openapi_types = {
            'items': List[CampaignSound],
            'limit': int,
            'offset': int,
            'total_count': int
        }

        self.attribute_map = {
            'items': 'items',
            'limit': 'limit',
            'offset': 'offset',
            'total_count': 'totalCount'
        }

        self._items = items
        self._limit = limit
        self._offset = offset
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CampaignSoundPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CampaignSoundPage of this CampaignSoundPage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this CampaignSoundPage.


        :return: The items of this CampaignSoundPage.
        :rtype: List[CampaignSound]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CampaignSoundPage.


        :param items: The items of this CampaignSoundPage.
        :type items: List[CampaignSound]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this CampaignSoundPage.

        A maximum number of returned items. If items.size() < limit assume no more items

        :return: The limit of this CampaignSoundPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CampaignSoundPage.

        A maximum number of returned items. If items.size() < limit assume no more items

        :param limit: The limit of this CampaignSoundPage.
        :type limit: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this CampaignSoundPage.

        An offset from a start of paging source

        :return: The offset of this CampaignSoundPage.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CampaignSoundPage.

        An offset from a start of paging source

        :param offset: The offset of this CampaignSoundPage.
        :type offset: int
        """

        self._offset = offset

    @property
    def total_count(self):
        """Gets the total_count of this CampaignSoundPage.

        Total count of available results. -1 if unknown

        :return: The total_count of this CampaignSoundPage.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CampaignSoundPage.

        Total count of available results. -1 if unknown

        :param total_count: The total_count of this CampaignSoundPage.
        :type total_count: int
        """

        self._total_count = total_count
