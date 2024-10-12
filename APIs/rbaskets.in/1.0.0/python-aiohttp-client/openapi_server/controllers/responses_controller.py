from typing import List, Dict
from aiohttp import web

from openapi_server.models.response import Response
from openapi_server import util


async def api_baskets_name_responses_method_get(request: web.Request, name, method) -> web.Response:
    """Get response settings

    Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

    :param name: The basket name
    :type name: str
    :param method: The HTTP method this response is configured for
    :type method: str

    """
    return web.Response(status=200)


async def api_baskets_name_responses_method_put(request: web.Request, name, method, response) -> web.Response:
    """Update response settings

    Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

    :param name: The basket name
    :type name: str
    :param method: The HTTP method this response is configured for
    :type method: str
    :param response: HTTP response configuration
    :type response: dict | bytes

    """
    response = Response.from_dict(response)
    return web.Response(status=200)


async def baskets_name_responses_method_get(request: web.Request, name, method) -> web.Response:
    """Get response settings

    Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

    :param name: The basket name
    :type name: str
    :param method: The HTTP method this response is configured for
    :type method: str

    """
    return web.Response(status=200)


async def baskets_name_responses_method_put(request: web.Request, name, method, response) -> web.Response:
    """Update response settings

    Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

    :param name: The basket name
    :type name: str
    :param method: The HTTP method this response is configured for
    :type method: str
    :param response: HTTP response configuration
    :type response: dict | bytes

    """
    response = Response.from_dict(response)
    return web.Response(status=200)
