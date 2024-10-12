from typing import List, Dict
from aiohttp import web

from openapi_server.models.component_type_representation import ComponentTypeRepresentation
from openapi_server import util


async def realm_client_registration_policy_providers_get(request: web.Request, realm) -> web.Response:
    """Base path for retrieve providers with the configProperties properly filled

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)
