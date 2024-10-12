from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_log_response import ListLogResponse
from openapi_server.models.serverless_v1_service_environment_log import ServerlessV1ServiceEnvironmentLog
from openapi_server import util


async def fetch_log(request: web.Request, service_sid, environment_sid, sid) -> web.Response:
    """fetch_log

    Retrieve a specific log.

    :param service_sid: The SID of the Service to fetch the Log resource from.
    :type service_sid: str
    :param environment_sid: The SID of the environment with the Log resource to fetch.
    :type environment_sid: str
    :param sid: The SID of the Log resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_log(request: web.Request, service_sid, environment_sid, function_sid=None, start_date=None, end_date=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_log

    Retrieve a list of all logs.

    :param service_sid: The SID of the Service to read the Log resource from.
    :type service_sid: str
    :param environment_sid: The SID of the environment with the Log resources to read.
    :type environment_sid: str
    :param function_sid: The SID of the function whose invocation produced the Log resources to read.
    :type function_sid: str
    :param start_date: The date/time (in GMT, ISO 8601) after which the Log resources must have been created. Defaults to 1 day prior to current date/time.
    :type start_date: str
    :param end_date: The date/time (in GMT, ISO 8601) before which the Log resources must have been created. Defaults to current date/time.
    :type end_date: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
