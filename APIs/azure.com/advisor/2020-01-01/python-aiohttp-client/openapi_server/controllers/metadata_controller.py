from typing import List, Dict
from aiohttp import web

from openapi_server.models.arm_error_response_body import ARMErrorResponseBody
from openapi_server.models.metadata_entity import MetadataEntity
from openapi_server.models.metadata_entity_list_result import MetadataEntityListResult
from openapi_server import util


async def recommendation_metadata_get(request: web.Request, name, api_version) -> web.Response:
    """Gets the metadata entity.

    

    :param name: Name of metadata entity.
    :type name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendation_metadata_list(request: web.Request, api_version) -> web.Response:
    """Gets the list of metadata entities.

    

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
