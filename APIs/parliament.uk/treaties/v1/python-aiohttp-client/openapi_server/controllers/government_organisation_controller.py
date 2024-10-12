from typing import List, Dict
from aiohttp import web

from openapi_server.models.government_organisation_resource_collection import GovernmentOrganisationResourceCollection
from openapi_server import util


async def get_organisations(request: web.Request, ) -> web.Response:
    """Returns all government organisations.

    


    """
    return web.Response(status=200)
