from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def financials_event_costs0_get(request: web.Request, api_key, filter_by_event_id=None, filter_by_event_start_date_greater_than_or_equal_to=None, filter_by_event_start_date_smaller_than_or_equal_to=None, filter_by_event_end_date_greater_than_or_equal_to=None, filter_by_event_end_date_smaller_than_or_equal_to=None) -> web.Response:
    """financials_event_costs0_get

    Retrieve event costs

    :param api_key: 
    :type api_key: str
    :param filter_by_event_id: Id of a specific event that you would like to retrieve costs for.
    :type filter_by_event_id: 
    :param filter_by_event_start_date_greater_than_or_equal_to: Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_event_start_date_greater_than_or_equal_to: str
    :param filter_by_event_start_date_smaller_than_or_equal_to: Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_event_start_date_smaller_than_or_equal_to: str
    :param filter_by_event_end_date_greater_than_or_equal_to: Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_event_end_date_greater_than_or_equal_to: str
    :param filter_by_event_end_date_smaller_than_or_equal_to: Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_event_end_date_smaller_than_or_equal_to: str

    """
    filter_by_event_start_date_greater_than_or_equal_to = util.deserialize_date(filter_by_event_start_date_greater_than_or_equal_to)
    filter_by_event_start_date_smaller_than_or_equal_to = util.deserialize_date(filter_by_event_start_date_smaller_than_or_equal_to)
    filter_by_event_end_date_greater_than_or_equal_to = util.deserialize_date(filter_by_event_end_date_greater_than_or_equal_to)
    filter_by_event_end_date_smaller_than_or_equal_to = util.deserialize_date(filter_by_event_end_date_smaller_than_or_equal_to)
    return web.Response(status=200)


async def financials_misc_annual_expense_costs0_get(request: web.Request, api_key, budget_year=None) -> web.Response:
    """financials_misc_annual_expense_costs0_get

    Retrieve Miscellaneous Annual Expense Costs

    :param api_key: 
    :type api_key: str
    :param budget_year: The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023).
    :type budget_year: 

    """
    return web.Response(status=200)
