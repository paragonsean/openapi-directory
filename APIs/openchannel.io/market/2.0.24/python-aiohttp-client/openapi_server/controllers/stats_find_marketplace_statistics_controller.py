from typing import List, Dict
from aiohttp import web

from openapi_server.models.total import Total
from openapi_server import util


async def stats_increment_field_post(request: web.Request, _field, app_id, user_id=None, value=None, _date=None) -> web.Response:
    """Increments a statistics field

    increment a statistics field

    :param _field: The field to be incremented
    :type _field: str
    :param app_id: The id of the app associated with this statistic value
    :type app_id: str
    :param user_id: The id of the user that is performing the action
    :type user_id: str
    :param value: The increment amount. Default is 1 if no value is provided.
    :type value: int
    :param _date: The date (in millis) for when this increment occurred. The default is the current date if no value is provided.
    :type _date: int

    """
    return web.Response(status=200)


async def stats_series_period_fields_get(request: web.Request, period, fields, start=None, end=None, query=None) -> web.Response:
    """Return a timeseries for a particular field

    Return a timeseries nested array containing date and value. Example: [[1406520000000,2],[1406606400000,34],[1406692800000,245],...]

    :param period: The period for the series (day or month)
    :type period: str
    :param fields: The field to be graphed. This also be a comma separated list of fields and the result will be a single timeseries containing the sum of all fields.
    :type fields: str
    :param start: The start date for this series (in millis)
    :type start: int
    :param end: The end date for this series (in millis)
    :type end: int
    :param query: A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112
    :type query: str

    """
    return web.Response(status=200)


async def stats_total_get(request: web.Request, fields, query=None, start=None, end=None) -> web.Response:
    """Returns the total number of events for a particular field.

    

    :param fields: A comma seperated list of all the fields to be returned in the total (available by default: dislikes, likes, reviews, totalSales, developerSales, marketplaceSales, downloads, ownerships, views)
    :type fields: str
    :param query: A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112
    :type query: str
    :param start: The start date for this total (in millis)
    :type start: int
    :param end: The end date for this total (in millis)
    :type end: int

    """
    return web.Response(status=200)
