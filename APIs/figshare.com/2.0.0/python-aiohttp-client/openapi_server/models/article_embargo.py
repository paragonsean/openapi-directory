# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ArticleEmbargo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, embargo_date: str=None, embargo_options: List[object]=None, embargo_reason: str=None, embargo_title: str=None, embargo_type: str=None, is_embargoed: bool=None):
        """ArticleEmbargo - a model defined in OpenAPI

        :param embargo_date: The embargo_date of this ArticleEmbargo.
        :param embargo_options: The embargo_options of this ArticleEmbargo.
        :param embargo_reason: The embargo_reason of this ArticleEmbargo.
        :param embargo_title: The embargo_title of this ArticleEmbargo.
        :param embargo_type: The embargo_type of this ArticleEmbargo.
        :param is_embargoed: The is_embargoed of this ArticleEmbargo.
        """
        self.openapi_types = {
            'embargo_date': str,
            'embargo_options': List[object],
            'embargo_reason': str,
            'embargo_title': str,
            'embargo_type': str,
            'is_embargoed': bool
        }

        self.attribute_map = {
            'embargo_date': 'embargo_date',
            'embargo_options': 'embargo_options',
            'embargo_reason': 'embargo_reason',
            'embargo_title': 'embargo_title',
            'embargo_type': 'embargo_type',
            'is_embargoed': 'is_embargoed'
        }

        self._embargo_date = embargo_date
        self._embargo_options = embargo_options
        self._embargo_reason = embargo_reason
        self._embargo_title = embargo_title
        self._embargo_type = embargo_type
        self._is_embargoed = is_embargoed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArticleEmbargo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArticleEmbargo of this ArticleEmbargo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def embargo_date(self):
        """Gets the embargo_date of this ArticleEmbargo.

        Date when embargo lifts

        :return: The embargo_date of this ArticleEmbargo.
        :rtype: str
        """
        return self._embargo_date

    @embargo_date.setter
    def embargo_date(self, embargo_date):
        """Sets the embargo_date of this ArticleEmbargo.

        Date when embargo lifts

        :param embargo_date: The embargo_date of this ArticleEmbargo.
        :type embargo_date: str
        """
        if embargo_date is None:
            raise ValueError("Invalid value for `embargo_date`, must not be `None`")

        self._embargo_date = embargo_date

    @property
    def embargo_options(self):
        """Gets the embargo_options of this ArticleEmbargo.

        List of embargo permissions that are associated with the article. If the type is logged_in and the group_ids list is empty, then the whole institution can see the article; if there are multiple group_ids, then only users that are under those groups can see the article.

        :return: The embargo_options of this ArticleEmbargo.
        :rtype: List[object]
        """
        return self._embargo_options

    @embargo_options.setter
    def embargo_options(self, embargo_options):
        """Sets the embargo_options of this ArticleEmbargo.

        List of embargo permissions that are associated with the article. If the type is logged_in and the group_ids list is empty, then the whole institution can see the article; if there are multiple group_ids, then only users that are under those groups can see the article.

        :param embargo_options: The embargo_options of this ArticleEmbargo.
        :type embargo_options: List[object]
        """
        if embargo_options is None:
            raise ValueError("Invalid value for `embargo_options`, must not be `None`")

        self._embargo_options = embargo_options

    @property
    def embargo_reason(self):
        """Gets the embargo_reason of this ArticleEmbargo.

        Reason for embargo

        :return: The embargo_reason of this ArticleEmbargo.
        :rtype: str
        """
        return self._embargo_reason

    @embargo_reason.setter
    def embargo_reason(self, embargo_reason):
        """Sets the embargo_reason of this ArticleEmbargo.

        Reason for embargo

        :param embargo_reason: The embargo_reason of this ArticleEmbargo.
        :type embargo_reason: str
        """
        if embargo_reason is None:
            raise ValueError("Invalid value for `embargo_reason`, must not be `None`")

        self._embargo_reason = embargo_reason

    @property
    def embargo_title(self):
        """Gets the embargo_title of this ArticleEmbargo.

        Title for embargo

        :return: The embargo_title of this ArticleEmbargo.
        :rtype: str
        """
        return self._embargo_title

    @embargo_title.setter
    def embargo_title(self, embargo_title):
        """Sets the embargo_title of this ArticleEmbargo.

        Title for embargo

        :param embargo_title: The embargo_title of this ArticleEmbargo.
        :type embargo_title: str
        """
        if embargo_title is None:
            raise ValueError("Invalid value for `embargo_title`, must not be `None`")

        self._embargo_title = embargo_title

    @property
    def embargo_type(self):
        """Gets the embargo_type of this ArticleEmbargo.

        Embargo type

        :return: The embargo_type of this ArticleEmbargo.
        :rtype: str
        """
        return self._embargo_type

    @embargo_type.setter
    def embargo_type(self, embargo_type):
        """Sets the embargo_type of this ArticleEmbargo.

        Embargo type

        :param embargo_type: The embargo_type of this ArticleEmbargo.
        :type embargo_type: str
        """
        if embargo_type is None:
            raise ValueError("Invalid value for `embargo_type`, must not be `None`")

        self._embargo_type = embargo_type

    @property
    def is_embargoed(self):
        """Gets the is_embargoed of this ArticleEmbargo.

        True if embargoed

        :return: The is_embargoed of this ArticleEmbargo.
        :rtype: bool
        """
        return self._is_embargoed

    @is_embargoed.setter
    def is_embargoed(self, is_embargoed):
        """Sets the is_embargoed of this ArticleEmbargo.

        True if embargoed

        :param is_embargoed: The is_embargoed of this ArticleEmbargo.
        :type is_embargoed: bool
        """
        if is_embargoed is None:
            raise ValueError("Invalid value for `is_embargoed`, must not be `None`")

        self._is_embargoed = is_embargoed
