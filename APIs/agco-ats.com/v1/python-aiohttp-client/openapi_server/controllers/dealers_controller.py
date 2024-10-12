from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_dealer import APIPagedResponseDealerDBModelsDealer
from openapi_server.models.dealer_db_models_dealer import DealerDBModelsDealer
from openapi_server import util


async def dealers_get_dealerby_dealer_code(request: web.Request, dealer_code) -> web.Response:
    """Lookup a dealer using a dealer code.

    No Documentation Found.

    :param dealer_code: The Dealer Code to Search for
    :type dealer_code: str

    """
    return web.Response(status=200)


async def dealers_get_dealers(request: web.Request, brand=None, shipping_country=None, dealer_name=None, limit=None, offset=None) -> web.Response:
    """Get a list of dealers.

    No Documentation Found.

    :param brand: The brand to filter by.
    :type brand: str
    :param shipping_country: The country to filter by.
    :type shipping_country: str
    :param dealer_name: The partial Dealer Name to filter by. Wildcard supported (*).
    :type dealer_name: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)
