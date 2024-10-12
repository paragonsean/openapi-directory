from typing import List, Dict
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.country_summary import CountrySummary
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server import util


async def get_countries(request: web.Request, market_id, region_type_id=None, region_name=None, sort=None, order=None) -> web.Response:
    """Retrieves summary country information for the provided marketId and filters

    Authorization is not required

    :param market_id: MarketId in which the request is being made, and for which responses should be localized
    :type market_id: str
    :param region_type_id: Restrict countries to this region type; required if regionName is supplied
    :type region_type_id: int
    :param region_name: Restrict countries to this region name; required if regionTypeId is supplied
    :type region_name: str
    :param sort: The term to sort the result countries by.
    :type sort: str
    :param order: The direction to sort the result countries by.
    :type order: str

    """
    return web.Response(status=200)


async def get_country(request: web.Request, country_key, market_id, sort=None, order=None) -> web.Response:
    """Retrieves country and summary state information for provided countryKey

    Authorization is not required

    :param country_key: The country key
    :type country_key: str
    :param market_id: MarketId in which the request is being made, and for which responses should be localized
    :type market_id: str
    :param sort: The term to sort the result country states by.
    :type sort: str
    :param order: The direction to sort the result country states by.
    :type order: str

    """
    return web.Response(status=200)
