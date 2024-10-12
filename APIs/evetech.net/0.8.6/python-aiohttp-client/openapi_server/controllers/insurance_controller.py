from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_insurance_prices200_ok import GetInsurancePrices200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_insurance_prices(request: web.Request, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """List insurance levels

    Return available insurance levels for all ship types  --- Alternate route: &#x60;/dev/insurance/prices/&#x60;  Alternate route: &#x60;/legacy/insurance/prices/&#x60;  Alternate route: &#x60;/v1/insurance/prices/&#x60;  --- This route is cached for up to 3600 seconds

    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str

    """
    return web.Response(status=200)
