from typing import List, Dict
from aiohttp import web

from openapi_server.models.proxy import Proxy
from openapi_server import util


async def proxy_get(request: web.Request, correlation_id, token=None, address=None, port=None, protocol=None, access_type=None, response_time=None, is_ssl=None, uptime=None, country=None, continent=None, timezone=None, last_tested=None) -> web.Response:
    """Gets a random proxy for chosen parameters.

    

    :param correlation_id: Correlation Id header field
    :type correlation_id: str
    :param token: 
    :type token: str
    :param address: 
    :type address: str
    :param port: 
    :type port: str
    :param protocol: 
    :type protocol: str
    :param access_type: 
    :type access_type: str
    :param response_time: 
    :type response_time: str
    :param is_ssl: 
    :type is_ssl: str
    :param uptime: 
    :type uptime: str
    :param country: 
    :type country: str
    :param continent: 
    :type continent: str
    :param timezone: 
    :type timezone: str
    :param last_tested: 
    :type last_tested: str

    """
    return web.Response(status=200)
