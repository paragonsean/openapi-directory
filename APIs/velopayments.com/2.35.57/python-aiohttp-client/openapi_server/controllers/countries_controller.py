from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.payment_channel_rules_response import PaymentChannelRulesResponse
from openapi_server.models.supported_countries_response import SupportedCountriesResponse
from openapi_server.models.supported_countries_response_v2 import SupportedCountriesResponseV2
from openapi_server import util


async def list_payment_channel_rules_v1(request: web.Request, ) -> web.Response:
    """List Payment Channel Country Rules

    List the country specific payment channel rules.


    """
    return web.Response(status=200)


async def list_supported_countries_v1(request: web.Request, ) -> web.Response:
    """List Supported Countries

    &lt;p&gt;List the supported countries.&lt;/p&gt; &lt;p&gt;This version will be retired in March 2020. Use /v2/supportedCountries&lt;/p&gt; 


    """
    return web.Response(status=200)


async def list_supported_countries_v2(request: web.Request, ) -> web.Response:
    """List Supported Countries

    List the supported countries.


    """
    return web.Response(status=200)
