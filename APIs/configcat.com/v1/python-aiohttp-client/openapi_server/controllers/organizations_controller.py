from typing import List, Dict
from aiohttp import web

from openapi_server.models.organization_model import OrganizationModel
from openapi_server.models.organization_model_haljson import OrganizationModelHaljson
from openapi_server import util


async def get_organizations(request: web.Request, ) -> web.Response:
    """List Organizations

    This endpoint returns the list of the Organizations that belongs to the user.


    """
    return web.Response(status=200)
