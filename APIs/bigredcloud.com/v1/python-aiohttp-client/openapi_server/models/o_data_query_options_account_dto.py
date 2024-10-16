# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.filter_query_option import FilterQueryOption
from openapi_server.models.inline_count_query_option import InlineCountQueryOption
from openapi_server.models.o_data_query_context import ODataQueryContext
from openapi_server.models.o_data_raw_query_options import ODataRawQueryOptions
from openapi_server.models.order_by_query_option import OrderByQueryOption
from openapi_server.models.select_expand_query_option import SelectExpandQueryOption
from openapi_server.models.skip_query_option import SkipQueryOption
from openapi_server.models.top_query_option import TopQueryOption
from openapi_server import util


class ODataQueryOptionsAccountDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, context: ODataQueryContext=None, filter: FilterQueryOption=None, if_match: object=None, if_none_match: object=None, inline_count: InlineCountQueryOption=None, order_by: OrderByQueryOption=None, raw_values: ODataRawQueryOptions=None, request: object=None, select_expand: SelectExpandQueryOption=None, skip: SkipQueryOption=None, top: TopQueryOption=None, validator: object=None):
        """ODataQueryOptionsAccountDto - a model defined in OpenAPI

        :param context: The context of this ODataQueryOptionsAccountDto.
        :param filter: The filter of this ODataQueryOptionsAccountDto.
        :param if_match: The if_match of this ODataQueryOptionsAccountDto.
        :param if_none_match: The if_none_match of this ODataQueryOptionsAccountDto.
        :param inline_count: The inline_count of this ODataQueryOptionsAccountDto.
        :param order_by: The order_by of this ODataQueryOptionsAccountDto.
        :param raw_values: The raw_values of this ODataQueryOptionsAccountDto.
        :param request: The request of this ODataQueryOptionsAccountDto.
        :param select_expand: The select_expand of this ODataQueryOptionsAccountDto.
        :param skip: The skip of this ODataQueryOptionsAccountDto.
        :param top: The top of this ODataQueryOptionsAccountDto.
        :param validator: The validator of this ODataQueryOptionsAccountDto.
        """
        self.openapi_types = {
            'context': ODataQueryContext,
            'filter': FilterQueryOption,
            'if_match': object,
            'if_none_match': object,
            'inline_count': InlineCountQueryOption,
            'order_by': OrderByQueryOption,
            'raw_values': ODataRawQueryOptions,
            'request': object,
            'select_expand': SelectExpandQueryOption,
            'skip': SkipQueryOption,
            'top': TopQueryOption,
            'validator': object
        }

        self.attribute_map = {
            'context': 'Context',
            'filter': 'Filter',
            'if_match': 'IfMatch',
            'if_none_match': 'IfNoneMatch',
            'inline_count': 'InlineCount',
            'order_by': 'OrderBy',
            'raw_values': 'RawValues',
            'request': 'Request',
            'select_expand': 'SelectExpand',
            'skip': 'Skip',
            'top': 'Top',
            'validator': 'Validator'
        }

        self._context = context
        self._filter = filter
        self._if_match = if_match
        self._if_none_match = if_none_match
        self._inline_count = inline_count
        self._order_by = order_by
        self._raw_values = raw_values
        self._request = request
        self._select_expand = select_expand
        self._skip = skip
        self._top = top
        self._validator = validator

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ODataQueryOptionsAccountDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ODataQueryOptions_AccountDto_ of this ODataQueryOptionsAccountDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self):
        """Gets the context of this ODataQueryOptionsAccountDto.


        :return: The context of this ODataQueryOptionsAccountDto.
        :rtype: ODataQueryContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ODataQueryOptionsAccountDto.


        :param context: The context of this ODataQueryOptionsAccountDto.
        :type context: ODataQueryContext
        """

        self._context = context

    @property
    def filter(self):
        """Gets the filter of this ODataQueryOptionsAccountDto.


        :return: The filter of this ODataQueryOptionsAccountDto.
        :rtype: FilterQueryOption
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ODataQueryOptionsAccountDto.


        :param filter: The filter of this ODataQueryOptionsAccountDto.
        :type filter: FilterQueryOption
        """

        self._filter = filter

    @property
    def if_match(self):
        """Gets the if_match of this ODataQueryOptionsAccountDto.


        :return: The if_match of this ODataQueryOptionsAccountDto.
        :rtype: object
        """
        return self._if_match

    @if_match.setter
    def if_match(self, if_match):
        """Sets the if_match of this ODataQueryOptionsAccountDto.


        :param if_match: The if_match of this ODataQueryOptionsAccountDto.
        :type if_match: object
        """

        self._if_match = if_match

    @property
    def if_none_match(self):
        """Gets the if_none_match of this ODataQueryOptionsAccountDto.


        :return: The if_none_match of this ODataQueryOptionsAccountDto.
        :rtype: object
        """
        return self._if_none_match

    @if_none_match.setter
    def if_none_match(self, if_none_match):
        """Sets the if_none_match of this ODataQueryOptionsAccountDto.


        :param if_none_match: The if_none_match of this ODataQueryOptionsAccountDto.
        :type if_none_match: object
        """

        self._if_none_match = if_none_match

    @property
    def inline_count(self):
        """Gets the inline_count of this ODataQueryOptionsAccountDto.


        :return: The inline_count of this ODataQueryOptionsAccountDto.
        :rtype: InlineCountQueryOption
        """
        return self._inline_count

    @inline_count.setter
    def inline_count(self, inline_count):
        """Sets the inline_count of this ODataQueryOptionsAccountDto.


        :param inline_count: The inline_count of this ODataQueryOptionsAccountDto.
        :type inline_count: InlineCountQueryOption
        """

        self._inline_count = inline_count

    @property
    def order_by(self):
        """Gets the order_by of this ODataQueryOptionsAccountDto.


        :return: The order_by of this ODataQueryOptionsAccountDto.
        :rtype: OrderByQueryOption
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ODataQueryOptionsAccountDto.


        :param order_by: The order_by of this ODataQueryOptionsAccountDto.
        :type order_by: OrderByQueryOption
        """

        self._order_by = order_by

    @property
    def raw_values(self):
        """Gets the raw_values of this ODataQueryOptionsAccountDto.


        :return: The raw_values of this ODataQueryOptionsAccountDto.
        :rtype: ODataRawQueryOptions
        """
        return self._raw_values

    @raw_values.setter
    def raw_values(self, raw_values):
        """Sets the raw_values of this ODataQueryOptionsAccountDto.


        :param raw_values: The raw_values of this ODataQueryOptionsAccountDto.
        :type raw_values: ODataRawQueryOptions
        """

        self._raw_values = raw_values

    @property
    def request(self):
        """Gets the request of this ODataQueryOptionsAccountDto.


        :return: The request of this ODataQueryOptionsAccountDto.
        :rtype: object
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this ODataQueryOptionsAccountDto.


        :param request: The request of this ODataQueryOptionsAccountDto.
        :type request: object
        """

        self._request = request

    @property
    def select_expand(self):
        """Gets the select_expand of this ODataQueryOptionsAccountDto.


        :return: The select_expand of this ODataQueryOptionsAccountDto.
        :rtype: SelectExpandQueryOption
        """
        return self._select_expand

    @select_expand.setter
    def select_expand(self, select_expand):
        """Sets the select_expand of this ODataQueryOptionsAccountDto.


        :param select_expand: The select_expand of this ODataQueryOptionsAccountDto.
        :type select_expand: SelectExpandQueryOption
        """

        self._select_expand = select_expand

    @property
    def skip(self):
        """Gets the skip of this ODataQueryOptionsAccountDto.


        :return: The skip of this ODataQueryOptionsAccountDto.
        :rtype: SkipQueryOption
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this ODataQueryOptionsAccountDto.


        :param skip: The skip of this ODataQueryOptionsAccountDto.
        :type skip: SkipQueryOption
        """

        self._skip = skip

    @property
    def top(self):
        """Gets the top of this ODataQueryOptionsAccountDto.


        :return: The top of this ODataQueryOptionsAccountDto.
        :rtype: TopQueryOption
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this ODataQueryOptionsAccountDto.


        :param top: The top of this ODataQueryOptionsAccountDto.
        :type top: TopQueryOption
        """

        self._top = top

    @property
    def validator(self):
        """Gets the validator of this ODataQueryOptionsAccountDto.


        :return: The validator of this ODataQueryOptionsAccountDto.
        :rtype: object
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """Sets the validator of this ODataQueryOptionsAccountDto.


        :param validator: The validator of this ODataQueryOptionsAccountDto.
        :type validator: object
        """

        self._validator = validator
