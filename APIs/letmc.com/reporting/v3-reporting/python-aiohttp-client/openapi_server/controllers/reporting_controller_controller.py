from typing import List, Dict
from aiohttp import web

from openapi_server.models.reporting_property_mortgage_model_results import ReportingPropertyMortgageModelResults
from openapi_server.models.reporting_receivership_case_model_results import ReportingReceivershipCaseModelResults
from openapi_server import util


async def reporting_controller_mortgages_by_created_date(request: web.Request, short_name, branch_id, start_date, offset, count) -> web.Response:
    """Return a collection of mortgages by created date from a specific date

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param start_date: The date to search from.
    :type start_date: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)


async def reporting_controller_mortgages_by_updated_date(request: web.Request, short_name, branch_id, start_date, offset, count) -> web.Response:
    """Return a collection of all mortgages updated from a specific date

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param start_date: The date to search from.
    :type start_date: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)


async def reporting_controller_repossessions_by_created_date(request: web.Request, short_name, branch_id, start_date, offset, count) -> web.Response:
    """Return a collection of repossessions by created date from a specific date

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param start_date: The date to search from.
    :type start_date: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)


async def reporting_controller_repossessions_by_updated_date(request: web.Request, short_name, branch_id, start_date, offset, count) -> web.Response:
    """Return a collection of all reposessions updated from a specific date

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param start_date: The date to search from.
    :type start_date: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)
