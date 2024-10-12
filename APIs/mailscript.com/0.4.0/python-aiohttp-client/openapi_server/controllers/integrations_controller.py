from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_integrations_response import GetAllIntegrationsResponse
from openapi_server import util


async def delete_integration(request: web.Request, integration) -> web.Response:
    """Delete an integration

    

    :param integration: ID of the integration
    :type integration: str

    """
    return web.Response(status=200)


async def get_all_integrations(request: web.Request, ) -> web.Response:
    """Get all integrations for the user

    


    """
    return web.Response(status=200)
