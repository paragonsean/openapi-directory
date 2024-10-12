from typing import List, Dict
from aiohttp import web

from openapi_server.models.cross_region_restore_request_resource import CrossRegionRestoreRequestResource
from openapi_server import util


async def cross_region_restore_trigger(request: web.Request, api_version, azure_region, subscription_id, parameters) -> web.Response:
    """Restores the specified backed up data in a different region as compared to where the data is backed up.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: resource cross region restore request
    :type parameters: dict | bytes

    """
    parameters = CrossRegionRestoreRequestResource.from_dict(parameters)
    return web.Response(status=200)
