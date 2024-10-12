from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_company_repository_v1_save_post_request import CompanyCompanyRepositoryV1SavePostRequest
from openapi_server.models.company_data_company_interface import CompanyDataCompanyInterface
from openapi_server.models.company_data_company_search_results_interface import CompanyDataCompanySearchResultsInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_company_repository_v1_get_list_get(request: web.Request, search_criteria_filter_groups_0_filters_0_field=None, search_criteria_filter_groups_0_filters_0_value=None, search_criteria_filter_groups_0_filters_0_condition_type=None, search_criteria_sort_orders_0_field=None, search_criteria_sort_orders_0_direction=None, search_criteria_page_size=None, search_criteria_current_page=None) -> web.Response:
    """company/

    Returns the list of companies. The list is an array of objects, and detailed information about item attributes might not be included.

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


async def company_company_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """company/

    Create or update a company account.

    :param body: 
    :type body: dict | bytes

    """
    body = CompanyCompanyRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
