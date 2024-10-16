# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ExpenseFilesExpenseFileIdPut200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: object=None, success: bool=True):
        """ExpenseFilesExpenseFileIdPut200Response - a model defined in OpenAPI

        :param data: The data of this ExpenseFilesExpenseFileIdPut200Response.
        :param success: The success of this ExpenseFilesExpenseFileIdPut200Response.
        """
        self.openapi_types = {
            'data': object,
            'success': bool
        }

        self.attribute_map = {
            'data': 'data',
            'success': 'success'
        }

        self._data = data
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpenseFilesExpenseFileIdPut200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _expense_files__expense_file_id__put_200_response of this ExpenseFilesExpenseFileIdPut200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ExpenseFilesExpenseFileIdPut200Response.


        :return: The data of this ExpenseFilesExpenseFileIdPut200Response.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ExpenseFilesExpenseFileIdPut200Response.


        :param data: The data of this ExpenseFilesExpenseFileIdPut200Response.
        :type data: object
        """

        self._data = data

    @property
    def success(self):
        """Gets the success of this ExpenseFilesExpenseFileIdPut200Response.


        :return: The success of this ExpenseFilesExpenseFileIdPut200Response.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ExpenseFilesExpenseFileIdPut200Response.


        :param success: The success of this ExpenseFilesExpenseFileIdPut200Response.
        :type success: bool
        """

        self._success = success
