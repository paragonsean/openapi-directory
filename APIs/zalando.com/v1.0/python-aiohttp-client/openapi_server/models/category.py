# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Category(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, child_keys: List[str]=None, cid: int=None, hidden: bool=None, key: str=None, name: str=None, outlet: bool=None, parent_key: str=None, suggested_filters: List[str]=None, target_group: str=None, type: str=None):
        """Category - a model defined in OpenAPI

        :param child_keys: The child_keys of this Category.
        :param cid: The cid of this Category.
        :param hidden: The hidden of this Category.
        :param key: The key of this Category.
        :param name: The name of this Category.
        :param outlet: The outlet of this Category.
        :param parent_key: The parent_key of this Category.
        :param suggested_filters: The suggested_filters of this Category.
        :param target_group: The target_group of this Category.
        :param type: The type of this Category.
        """
        self.openapi_types = {
            'child_keys': List[str],
            'cid': int,
            'hidden': bool,
            'key': str,
            'name': str,
            'outlet': bool,
            'parent_key': str,
            'suggested_filters': List[str],
            'target_group': str,
            'type': str
        }

        self.attribute_map = {
            'child_keys': 'childKeys',
            'cid': 'cid',
            'hidden': 'hidden',
            'key': 'key',
            'name': 'name',
            'outlet': 'outlet',
            'parent_key': 'parentKey',
            'suggested_filters': 'suggestedFilters',
            'target_group': 'targetGroup',
            'type': 'type'
        }

        self._child_keys = child_keys
        self._cid = cid
        self._hidden = hidden
        self._key = key
        self._name = name
        self._outlet = outlet
        self._parent_key = parent_key
        self._suggested_filters = suggested_filters
        self._target_group = target_group
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Category':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Category of this Category.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def child_keys(self):
        """Gets the child_keys of this Category.

        The list of keys of the child categories

        :return: The child_keys of this Category.
        :rtype: List[str]
        """
        return self._child_keys

    @child_keys.setter
    def child_keys(self, child_keys):
        """Sets the child_keys of this Category.

        The list of keys of the child categories

        :param child_keys: The child_keys of this Category.
        :type child_keys: List[str]
        """
        if child_keys is None:
            raise ValueError("Invalid value for `child_keys`, must not be `None`")
        if child_keys is not None and len(child_keys) < 0:
            raise ValueError("Invalid value for `child_keys`, number of items must be greater than or equal to `0`")

        self._child_keys = child_keys

    @property
    def cid(self):
        """Gets the cid of this Category.

        The numeric ID for a category.

        :return: The cid of this Category.
        :rtype: int
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this Category.

        The numeric ID for a category.

        :param cid: The cid of this Category.
        :type cid: int
        """

        self._cid = cid

    @property
    def hidden(self):
        """Gets the hidden of this Category.

        The category is hidden and not shown on the Zalando web shop

        :return: The hidden of this Category.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Category.

        The category is hidden and not shown on the Zalando web shop

        :param hidden: The hidden of this Category.
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def key(self):
        """Gets the key of this Category.

        The unique key for a category

        :return: The key of this Category.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Category.

        The unique key for a category

        :param key: The key of this Category.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """Gets the name of this Category.

        Name of the category

        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.

        Name of the category

        :param name: The name of this Category.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def outlet(self):
        """Gets the outlet of this Category.

        Containing articles are from last seasons

        :return: The outlet of this Category.
        :rtype: bool
        """
        return self._outlet

    @outlet.setter
    def outlet(self, outlet):
        """Sets the outlet of this Category.

        Containing articles are from last seasons

        :param outlet: The outlet of this Category.
        :type outlet: bool
        """

        self._outlet = outlet

    @property
    def parent_key(self):
        """Gets the parent_key of this Category.

        The key of the parent category

        :return: The parent_key of this Category.
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """Sets the parent_key of this Category.

        The key of the parent category

        :param parent_key: The parent_key of this Category.
        :type parent_key: str
        """

        self._parent_key = parent_key

    @property
    def suggested_filters(self):
        """Gets the suggested_filters of this Category.

        list of filter names that are reasonable to use within this category

        :return: The suggested_filters of this Category.
        :rtype: List[str]
        """
        return self._suggested_filters

    @suggested_filters.setter
    def suggested_filters(self, suggested_filters):
        """Sets the suggested_filters of this Category.

        list of filter names that are reasonable to use within this category

        :param suggested_filters: The suggested_filters of this Category.
        :type suggested_filters: List[str]
        """
        if suggested_filters is None:
            raise ValueError("Invalid value for `suggested_filters`, must not be `None`")
        if suggested_filters is not None and len(suggested_filters) < 1:
            raise ValueError("Invalid value for `suggested_filters`, number of items must be greater than or equal to `1`")

        self._suggested_filters = suggested_filters

    @property
    def target_group(self):
        """Gets the target_group of this Category.

        The target group of the articles from this category

        :return: The target_group of this Category.
        :rtype: str
        """
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        """Sets the target_group of this Category.

        The target group of the articles from this category

        :param target_group: The target_group of this Category.
        :type target_group: str
        """
        allowed_values = ["ALL", "WOMEN", "MEN", "KIDS"]  # noqa: E501
        if target_group not in allowed_values:
            raise ValueError(
                "Invalid value for `target_group` ({0}), must be one of {1}"
                .format(target_group, allowed_values)
            )

        self._target_group = target_group

    @property
    def type(self):
        """Gets the type of this Category.

        The type of the category.

        :return: The type of this Category.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Category.

        The type of the category.

        :param type: The type of this Category.
        :type type: str
        """

        self._type = type
