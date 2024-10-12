from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.farm_organization import FarmOrganization
from openapi_server import util


async def fetch_farm_organization_by_type_and_id(request: web.Request, farm_organization_type, farm_organization_id) -> web.Response:
    """Retrieve a specific farm organization by organization type and ID

    Retrieve a given **farm organization** by organization type and ID.

    :param farm_organization_type: Type of the farm organization.
    :type farm_organization_type: str
    :param farm_organization_id: Unique identifier of the farm organization.
    :type farm_organization_id: str
    :type farm_organization_id: str

    """
    return web.Response(status=200)
