from typing import List, Dict
from aiohttp import web

from openapi_server.models.series_membership_resource_collection import SeriesMembershipResourceCollection
from openapi_server import util


async def get_series_memberships(request: web.Request, ) -> web.Response:
    """Returns all series memberships.

    


    """
    return web.Response(status=200)
