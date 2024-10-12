from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_data_rma_interface import RmaDataRmaInterface
from openapi_server.models.rma_data_rma_search_result_interface import RmaDataRmaSearchResultInterface
from openapi_server.models.rma_rma_management_v1_save_rma_post_request import RmaRmaManagementV1SaveRmaPostRequest
from openapi_server import util


async def rma_rma_management_v1_save_rma_post(request: web.Request, body=None) -> web.Response:
    """returns

    Save RMA

    :param body: 
    :type body: dict | bytes

    """
    body = RmaRmaManagementV1SaveRmaPostRequest.from_dict(body)
    return web.Response(status=200)


async def rma_rma_management_v1_search_get(request: web.Request, search_criteria_filter_groups_0_filters_0_field=None, search_criteria_filter_groups_0_filters_0_value=None, search_criteria_filter_groups_0_filters_0_condition_type=None, search_criteria_sort_orders_0_field=None, search_criteria_sort_orders_0_direction=None, search_criteria_page_size=None, search_criteria_current_page=None) -> web.Response:
    """returns

    Return list of rma data objects based on search criteria

    :param search_criteria_filter_groups_0_filters_0_field: Field
    :type search_criteria_filter_groups_0_filters_0_field: str
    :param search_criteria_filter_groups_0_filters_0_value: Value
    :type search_criteria_filter_groups_0_filters_0_value: str
    :param search_criteria_filter_groups_0_filters_0_condition_type: Condition type
    :type search_criteria_filter_groups_0_filters_0_condition_type: str
    :param search_criteria_sort_orders_0_field: Sorting field.
    :type search_criteria_sort_orders_0_field: str
    :param search_criteria_sort_orders_0_direction: Sorting direction.
    :type search_criteria_sort_orders_0_direction: str
    :param search_criteria_page_size: Page size.
    :type search_criteria_page_size: int
    :param search_criteria_current_page: Current page.
    :type search_criteria_current_page: int

    """
    return web.Response(status=200)
