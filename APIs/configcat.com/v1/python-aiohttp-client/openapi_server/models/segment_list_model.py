# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.product_model import ProductModel
from openapi_server import util


class SegmentListModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: datetime=None, creator_email: str=None, creator_full_name: str=None, description: str=None, last_updater_email: str=None, last_updater_full_name: str=None, name: str=None, product: ProductModel=None, segment_id: str=None, updated_at: datetime=None, usage: int=None):
        """SegmentListModel - a model defined in OpenAPI

        :param created_at: The created_at of this SegmentListModel.
        :param creator_email: The creator_email of this SegmentListModel.
        :param creator_full_name: The creator_full_name of this SegmentListModel.
        :param description: The description of this SegmentListModel.
        :param last_updater_email: The last_updater_email of this SegmentListModel.
        :param last_updater_full_name: The last_updater_full_name of this SegmentListModel.
        :param name: The name of this SegmentListModel.
        :param product: The product of this SegmentListModel.
        :param segment_id: The segment_id of this SegmentListModel.
        :param updated_at: The updated_at of this SegmentListModel.
        :param usage: The usage of this SegmentListModel.
        """
        self.openapi_types = {
            'created_at': datetime,
            'creator_email': str,
            'creator_full_name': str,
            'description': str,
            'last_updater_email': str,
            'last_updater_full_name': str,
            'name': str,
            'product': ProductModel,
            'segment_id': str,
            'updated_at': datetime,
            'usage': int
        }

        self.attribute_map = {
            'created_at': 'createdAt',
            'creator_email': 'creatorEmail',
            'creator_full_name': 'creatorFullName',
            'description': 'description',
            'last_updater_email': 'lastUpdaterEmail',
            'last_updater_full_name': 'lastUpdaterFullName',
            'name': 'name',
            'product': 'product',
            'segment_id': 'segmentId',
            'updated_at': 'updatedAt',
            'usage': 'usage'
        }

        self._created_at = created_at
        self._creator_email = creator_email
        self._creator_full_name = creator_full_name
        self._description = description
        self._last_updater_email = last_updater_email
        self._last_updater_full_name = last_updater_full_name
        self._name = name
        self._product = product
        self._segment_id = segment_id
        self._updated_at = updated_at
        self._usage = usage

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SegmentListModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SegmentListModel of this SegmentListModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this SegmentListModel.


        :return: The created_at of this SegmentListModel.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SegmentListModel.


        :param created_at: The created_at of this SegmentListModel.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def creator_email(self):
        """Gets the creator_email of this SegmentListModel.


        :return: The creator_email of this SegmentListModel.
        :rtype: str
        """
        return self._creator_email

    @creator_email.setter
    def creator_email(self, creator_email):
        """Sets the creator_email of this SegmentListModel.


        :param creator_email: The creator_email of this SegmentListModel.
        :type creator_email: str
        """

        self._creator_email = creator_email

    @property
    def creator_full_name(self):
        """Gets the creator_full_name of this SegmentListModel.


        :return: The creator_full_name of this SegmentListModel.
        :rtype: str
        """
        return self._creator_full_name

    @creator_full_name.setter
    def creator_full_name(self, creator_full_name):
        """Sets the creator_full_name of this SegmentListModel.


        :param creator_full_name: The creator_full_name of this SegmentListModel.
        :type creator_full_name: str
        """

        self._creator_full_name = creator_full_name

    @property
    def description(self):
        """Gets the description of this SegmentListModel.


        :return: The description of this SegmentListModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SegmentListModel.


        :param description: The description of this SegmentListModel.
        :type description: str
        """

        self._description = description

    @property
    def last_updater_email(self):
        """Gets the last_updater_email of this SegmentListModel.


        :return: The last_updater_email of this SegmentListModel.
        :rtype: str
        """
        return self._last_updater_email

    @last_updater_email.setter
    def last_updater_email(self, last_updater_email):
        """Sets the last_updater_email of this SegmentListModel.


        :param last_updater_email: The last_updater_email of this SegmentListModel.
        :type last_updater_email: str
        """

        self._last_updater_email = last_updater_email

    @property
    def last_updater_full_name(self):
        """Gets the last_updater_full_name of this SegmentListModel.


        :return: The last_updater_full_name of this SegmentListModel.
        :rtype: str
        """
        return self._last_updater_full_name

    @last_updater_full_name.setter
    def last_updater_full_name(self, last_updater_full_name):
        """Sets the last_updater_full_name of this SegmentListModel.


        :param last_updater_full_name: The last_updater_full_name of this SegmentListModel.
        :type last_updater_full_name: str
        """

        self._last_updater_full_name = last_updater_full_name

    @property
    def name(self):
        """Gets the name of this SegmentListModel.


        :return: The name of this SegmentListModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SegmentListModel.


        :param name: The name of this SegmentListModel.
        :type name: str
        """

        self._name = name

    @property
    def product(self):
        """Gets the product of this SegmentListModel.


        :return: The product of this SegmentListModel.
        :rtype: ProductModel
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SegmentListModel.


        :param product: The product of this SegmentListModel.
        :type product: ProductModel
        """

        self._product = product

    @property
    def segment_id(self):
        """Gets the segment_id of this SegmentListModel.


        :return: The segment_id of this SegmentListModel.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this SegmentListModel.


        :param segment_id: The segment_id of this SegmentListModel.
        :type segment_id: str
        """

        self._segment_id = segment_id

    @property
    def updated_at(self):
        """Gets the updated_at of this SegmentListModel.


        :return: The updated_at of this SegmentListModel.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SegmentListModel.


        :param updated_at: The updated_at of this SegmentListModel.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def usage(self):
        """Gets the usage of this SegmentListModel.


        :return: The usage of this SegmentListModel.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this SegmentListModel.


        :param usage: The usage of this SegmentListModel.
        :type usage: int
        """

        self._usage = usage
