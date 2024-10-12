from typing import List, Dict
from aiohttp import web

from openapi_server.models.analytics_data_count_swagger_model import AnalyticsDataCountSwaggerModel
from openapi_server.models.analytics_data_swagger_model import AnalyticsDataSwaggerModel
from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def get_analytics_data_using_get(request: web.Request, api_key, stage, data_type, precision, start_date, end_date, keys=None) -> web.Response:
    """Returns the results of executed query defined by the parameters passed in

    

    :param api_key: apiKey
    :type api_key: str
    :param stage: stage
    :type stage: str
    :param data_type: dataType
    :type data_type: str
    :param precision: precision
    :type precision: str
    :param start_date: yyyy-MM-dd
    :type start_date: str
    :param end_date: yyyy-MM-dd
    :type end_date: str
    :param keys: the keys to select. For example \&quot;ReturningUsers\&quot;, \&quot;NewUsers\&quot;, etc
    :type keys: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def get_data_count_using_get(request: web.Request, api_key, stage, query_name) -> web.Response:
    """Returns the count of executed query

    

    :param api_key: apiKey
    :type api_key: str
    :param stage: stage
    :type stage: str
    :param query_name: queryName
    :type query_name: str

    """
    return web.Response(status=200)


async def get_retention_using_get(request: web.Request, api_key, stage) -> web.Response:
    """Returns the percentage of user retention over the last 30 days

    

    :param api_key: apiKey
    :type api_key: str
    :param stage: stage
    :type stage: str

    """
    return web.Response(status=200)
