# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.chart_axes_details import ChartAxesDetails
from openapi_server.models.chart_column_collections_details import ChartColumnCollectionsDetails
from openapi_server import util


class ChartColumnsDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, axis: ChartAxesDetails=None, axis_id: str=None, column_collection: ChartColumnCollectionsDetails=None, column_collection_id: str=None, date_created: datetime=None, date_modified: datetime=None, id: str=None, index: int=None, name: str=None, user_created: str=None, user_modified: str=None):
        """ChartColumnsDetails - a model defined in OpenAPI

        :param axis: The axis of this ChartColumnsDetails.
        :param axis_id: The axis_id of this ChartColumnsDetails.
        :param column_collection: The column_collection of this ChartColumnsDetails.
        :param column_collection_id: The column_collection_id of this ChartColumnsDetails.
        :param date_created: The date_created of this ChartColumnsDetails.
        :param date_modified: The date_modified of this ChartColumnsDetails.
        :param id: The id of this ChartColumnsDetails.
        :param index: The index of this ChartColumnsDetails.
        :param name: The name of this ChartColumnsDetails.
        :param user_created: The user_created of this ChartColumnsDetails.
        :param user_modified: The user_modified of this ChartColumnsDetails.
        """
        self.openapi_types = {
            'axis': ChartAxesDetails,
            'axis_id': str,
            'column_collection': ChartColumnCollectionsDetails,
            'column_collection_id': str,
            'date_created': datetime,
            'date_modified': datetime,
            'id': str,
            'index': int,
            'name': str,
            'user_created': str,
            'user_modified': str
        }

        self.attribute_map = {
            'axis': 'axis',
            'axis_id': 'axisId',
            'column_collection': 'columnCollection',
            'column_collection_id': 'columnCollectionId',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'id': 'id',
            'index': 'index',
            'name': 'name',
            'user_created': 'userCreated',
            'user_modified': 'userModified'
        }

        self._axis = axis
        self._axis_id = axis_id
        self._column_collection = column_collection
        self._column_collection_id = column_collection_id
        self._date_created = date_created
        self._date_modified = date_modified
        self._id = id
        self._index = index
        self._name = name
        self._user_created = user_created
        self._user_modified = user_modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChartColumnsDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Chart.Columns.Details of this ChartColumnsDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def axis(self):
        """Gets the axis of this ChartColumnsDetails.


        :return: The axis of this ChartColumnsDetails.
        :rtype: ChartAxesDetails
        """
        return self._axis

    @axis.setter
    def axis(self, axis):
        """Sets the axis of this ChartColumnsDetails.


        :param axis: The axis of this ChartColumnsDetails.
        :type axis: ChartAxesDetails
        """

        self._axis = axis

    @property
    def axis_id(self):
        """Gets the axis_id of this ChartColumnsDetails.


        :return: The axis_id of this ChartColumnsDetails.
        :rtype: str
        """
        return self._axis_id

    @axis_id.setter
    def axis_id(self, axis_id):
        """Sets the axis_id of this ChartColumnsDetails.


        :param axis_id: The axis_id of this ChartColumnsDetails.
        :type axis_id: str
        """

        self._axis_id = axis_id

    @property
    def column_collection(self):
        """Gets the column_collection of this ChartColumnsDetails.


        :return: The column_collection of this ChartColumnsDetails.
        :rtype: ChartColumnCollectionsDetails
        """
        return self._column_collection

    @column_collection.setter
    def column_collection(self, column_collection):
        """Sets the column_collection of this ChartColumnsDetails.


        :param column_collection: The column_collection of this ChartColumnsDetails.
        :type column_collection: ChartColumnCollectionsDetails
        """

        self._column_collection = column_collection

    @property
    def column_collection_id(self):
        """Gets the column_collection_id of this ChartColumnsDetails.


        :return: The column_collection_id of this ChartColumnsDetails.
        :rtype: str
        """
        return self._column_collection_id

    @column_collection_id.setter
    def column_collection_id(self, column_collection_id):
        """Sets the column_collection_id of this ChartColumnsDetails.


        :param column_collection_id: The column_collection_id of this ChartColumnsDetails.
        :type column_collection_id: str
        """

        self._column_collection_id = column_collection_id

    @property
    def date_created(self):
        """Gets the date_created of this ChartColumnsDetails.


        :return: The date_created of this ChartColumnsDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ChartColumnsDetails.


        :param date_created: The date_created of this ChartColumnsDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this ChartColumnsDetails.


        :return: The date_modified of this ChartColumnsDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ChartColumnsDetails.


        :param date_modified: The date_modified of this ChartColumnsDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def id(self):
        """Gets the id of this ChartColumnsDetails.


        :return: The id of this ChartColumnsDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartColumnsDetails.


        :param id: The id of this ChartColumnsDetails.
        :type id: str
        """

        self._id = id

    @property
    def index(self):
        """Gets the index of this ChartColumnsDetails.


        :return: The index of this ChartColumnsDetails.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ChartColumnsDetails.


        :param index: The index of this ChartColumnsDetails.
        :type index: int
        """

        self._index = index

    @property
    def name(self):
        """Gets the name of this ChartColumnsDetails.


        :return: The name of this ChartColumnsDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChartColumnsDetails.


        :param name: The name of this ChartColumnsDetails.
        :type name: str
        """

        self._name = name

    @property
    def user_created(self):
        """Gets the user_created of this ChartColumnsDetails.


        :return: The user_created of this ChartColumnsDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this ChartColumnsDetails.


        :param user_created: The user_created of this ChartColumnsDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this ChartColumnsDetails.


        :return: The user_modified of this ChartColumnsDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this ChartColumnsDetails.


        :param user_modified: The user_modified of this ChartColumnsDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified
