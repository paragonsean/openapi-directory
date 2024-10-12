from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.factory import Factory
from openapi_server.models.factory_repo_update import FactoryRepoUpdate
from openapi_server import util


async def factories_configure_factory_repo(request: web.Request, subscription_id, location_id, api_version, factory_repo_update) -> web.Response:
    """factories_configure_factory_repo

    Updates a factory&#39;s repo information.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param location_id: The location identifier.
    :type location_id: str
    :param api_version: The API version.
    :type api_version: str
    :param factory_repo_update: Update factory repo request definition.
    :type factory_repo_update: dict | bytes

    """
    factory_repo_update = FactoryRepoUpdate.from_dict(factory_repo_update)
    return web.Response(status=200)
