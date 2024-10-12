from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_entity import ApiEntity
from openapi_server.models.apis_collection import ApisCollection
from openapi_server import util


async def managed_apis_get(request: web.Request, location, api_name, subscription_id, api_version, export=None) -> web.Response:
    """Get managed API

    Gets a managed API.

    :param location: The location.
    :type location: str
    :param api_name: The managed API name.
    :type api_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param export: flag showing whether to export API definition in format specified by Accept header.
    :type export: bool

    """
    return web.Response(status=200)


async def managed_apis_list(request: web.Request, location, subscription_id, api_version) -> web.Response:
    """List managed Apis

    Gets a list of managed APIs.

    :param location: The location.
    :type location: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
