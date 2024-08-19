from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.policy_metadata import PolicyMetadata
from openapi_server.models.policy_metadata_collection import PolicyMetadataCollection
from openapi_server import util


async def policy_metadata_get_resource(request: web.Request, resource_name, api_version) -> web.Response:
    """policy_metadata_get_resource

    Get policy metadata resource.

    :param resource_name: The name of the policy metadata resource.
    :type resource_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_metadata_list(request: web.Request, api_version, top=None) -> web.Response:
    """policy_metadata_list

    Get a list of the policy metadata resources.

    :param api_version: Client Api Version.
    :type api_version: str
    :param top: Maximum number of records to return.
    :type top: int

    """
    return web.Response(status=200)
