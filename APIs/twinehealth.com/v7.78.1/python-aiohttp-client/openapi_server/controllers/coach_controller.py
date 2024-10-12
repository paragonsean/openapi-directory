from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_coach_response import FetchCoachResponse
from openapi_server.models.fetch_coaches_response import FetchCoachesResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server import util


async def fetch_coach(request: web.Request, id) -> web.Response:
    """Get a coach

    Get a coach record by id.

    :param id: Coach identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_coaches(request: web.Request, filter_groups=None, filter_organization=None) -> web.Response:
    """List coaches

    Get a list of coaches matching the specified filters.

    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str

    """
    return web.Response(status=200)
