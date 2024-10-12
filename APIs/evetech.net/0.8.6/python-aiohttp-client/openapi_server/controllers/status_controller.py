from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_status_ok import GetStatusOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_status(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Retrieve the uptime and player counts

    EVE Server status  --- Alternate route: &#x60;/dev/status/&#x60;  Alternate route: &#x60;/legacy/status/&#x60;  Alternate route: &#x60;/v1/status/&#x60;  --- This route is cached for up to 30 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
