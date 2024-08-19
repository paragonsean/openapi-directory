from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_accident_stats_accident_detail import TflApiPresentationEntitiesAccidentStatsAccidentDetail
from openapi_server import util


async def accident_stats_get(request: web.Request, year) -> web.Response:
    """Gets all accident details for accidents occuring in the specified year

    

    :param year: The year for which to filter the accidents on.
    :type year: int

    """
    return web.Response(status=200)
