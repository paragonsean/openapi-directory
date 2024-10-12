from typing import List, Dict
from aiohttp import web

from openapi_server.models.aad_properties_resource import AADPropertiesResource
from openapi_server import util


async def aad_properties_get(request: web.Request, api_version, azure_region, subscription_id) -> web.Response:
    """Fetches the AAD properties from target region BCM stamp.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
