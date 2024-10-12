from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_integrations_list200_response import GetIntegrationsList200Response
from openapi_server.models.integrations_billys_authenticate_post200_response import IntegrationsBillysAuthenticatePost200Response
from openapi_server.models.integrations_products_sync_get200_response import IntegrationsProductsSyncGet200Response
from openapi_server import util


async def get_integrations_contacts_sync(request: web.Request, ) -> web.Response:
    """Force Synchronization with ERP systems

    


    """
    return web.Response(status=200)


async def get_integrations_list(request: web.Request, ) -> web.Response:
    """Get integrations list

    


    """
    return web.Response(status=200)


async def get_integrations_view(request: web.Request, integration_id) -> web.Response:
    """View integration details

    

    :param integration_id: Automatically added
    :type integration_id: str

    """
    return web.Response(status=200)


async def integrations_billys_authenticate_post(request: web.Request, ) -> web.Response:
    """Authenticate to Billys

    


    """
    return web.Response(status=200)


async def integrations_products_sync_get(request: web.Request, ) -> web.Response:
    """Sync products from erp integration

    


    """
    return web.Response(status=200)
