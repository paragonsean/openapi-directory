# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.pagination import Pagination
from openapi_server.models.response_product_attribute_list_result import ResponseProductAttributeListResult
from openapi_server import util


class ModelResponseProductAttributeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_fields: object=None, custom_fields: object=None, pagination: Pagination=None, result: ResponseProductAttributeListResult=None, return_code: int=None, return_message: str=None):
        """ModelResponseProductAttributeList - a model defined in OpenAPI

        :param additional_fields: The additional_fields of this ModelResponseProductAttributeList.
        :param custom_fields: The custom_fields of this ModelResponseProductAttributeList.
        :param pagination: The pagination of this ModelResponseProductAttributeList.
        :param result: The result of this ModelResponseProductAttributeList.
        :param return_code: The return_code of this ModelResponseProductAttributeList.
        :param return_message: The return_message of this ModelResponseProductAttributeList.
        """
        self.openapi_types = {
            'additional_fields': object,
            'custom_fields': object,
            'pagination': Pagination,
            'result': ResponseProductAttributeListResult,
            'return_code': int,
            'return_message': str
        }

        self.attribute_map = {
            'additional_fields': 'additional_fields',
            'custom_fields': 'custom_fields',
            'pagination': 'pagination',
            'result': 'result',
            'return_code': 'return_code',
            'return_message': 'return_message'
        }

        self._additional_fields = additional_fields
        self._custom_fields = custom_fields
        self._pagination = pagination
        self._result = result
        self._return_code = return_code
        self._return_message = return_message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelResponseProductAttributeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Model_Response_Product_Attribute_List of this ModelResponseProductAttributeList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ModelResponseProductAttributeList.


        :return: The additional_fields of this ModelResponseProductAttributeList.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ModelResponseProductAttributeList.


        :param additional_fields: The additional_fields of this ModelResponseProductAttributeList.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ModelResponseProductAttributeList.


        :return: The custom_fields of this ModelResponseProductAttributeList.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ModelResponseProductAttributeList.


        :param custom_fields: The custom_fields of this ModelResponseProductAttributeList.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def pagination(self):
        """Gets the pagination of this ModelResponseProductAttributeList.


        :return: The pagination of this ModelResponseProductAttributeList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ModelResponseProductAttributeList.


        :param pagination: The pagination of this ModelResponseProductAttributeList.
        :type pagination: Pagination
        """

        self._pagination = pagination

    @property
    def result(self):
        """Gets the result of this ModelResponseProductAttributeList.


        :return: The result of this ModelResponseProductAttributeList.
        :rtype: ResponseProductAttributeListResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ModelResponseProductAttributeList.


        :param result: The result of this ModelResponseProductAttributeList.
        :type result: ResponseProductAttributeListResult
        """

        self._result = result

    @property
    def return_code(self):
        """Gets the return_code of this ModelResponseProductAttributeList.


        :return: The return_code of this ModelResponseProductAttributeList.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this ModelResponseProductAttributeList.


        :param return_code: The return_code of this ModelResponseProductAttributeList.
        :type return_code: int
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this ModelResponseProductAttributeList.


        :return: The return_message of this ModelResponseProductAttributeList.
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this ModelResponseProductAttributeList.


        :param return_message: The return_message of this ModelResponseProductAttributeList.
        :type return_message: str
        """

        self._return_message = return_message
