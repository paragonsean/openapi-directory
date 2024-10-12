from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_credit_data_credit_limit_search_results_interface import CompanyCreditDataCreditLimitSearchResultsInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_credit_credit_limit_repository_v1_get_list_get(request: web.Request, search_criteria_filter_groups_0_filters_0_field=None, search_criteria_filter_groups_0_filters_0_value=None, search_criteria_filter_groups_0_filters_0_condition_type=None, search_criteria_sort_orders_0_field=None, search_criteria_sort_orders_0_direction=None, search_criteria_page_size=None, search_criteria_current_page=None) -> web.Response:
    """companyCredits/

    Returns the list of credits for specified companies.

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
