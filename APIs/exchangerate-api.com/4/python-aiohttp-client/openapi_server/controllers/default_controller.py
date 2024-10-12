from typing import List, Dict
from aiohttp import web

from openapi_server.models.latest_base_currency_get200_response import LatestBaseCurrencyGet200Response
from openapi_server.models.latest_base_currency_get404_response import LatestBaseCurrencyGet404Response
from openapi_server import util


async def latest_base_currency_get(request: web.Request, base_currency) -> web.Response:
    """Returns latest exchange rates in parameter-supplied base currency.

    

    :param base_currency: **Base Currency**. *Example: USD*. You an use any of the ISO 4217 currency codes we support. See https://www.exchangerate-api.com/docs/supported-currencies
    :type base_currency: str

    """
    return web.Response(status=200)
