from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metadata_entity import MetadataEntity
from openapi_server.models.metadata_entity_list_result import MetadataEntityListResult
from openapi_server import util


async def metadata_get(request: web.Request, name, api_version) -> web.Response:
    """Gets the metadata entity.

    

    :param name: Name of metadata entity.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def metadata_list(request: web.Request, api_version) -> web.Response:
    """Gets the list of metadata entities.

    

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
