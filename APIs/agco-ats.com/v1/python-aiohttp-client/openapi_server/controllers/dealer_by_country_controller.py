from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_dealers_per_country import APIPagedResponseDealerDBModelsDealersPerCountry
from openapi_server import util


async def dealer_by_country_get_countries(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get a total count of dealers per country

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)
