from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.destination_core_config import DestinationCoreConfig
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.source_core_config import SourceCoreConfig
from openapi_server.models.source_discover_schema_read import SourceDiscoverSchemaRead
from openapi_server import util


async def execute_destination_check_connection(request: web.Request, body) -> web.Response:
    """Run check connection for a given destination configuration

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationCoreConfig.from_dict(body)
    return web.Response(status=200)


async def execute_source_check_connection(request: web.Request, body) -> web.Response:
    """Run check connection for a given source configuration

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceCoreConfig.from_dict(body)
    return web.Response(status=200)


async def execute_source_discover_schema(request: web.Request, body) -> web.Response:
    """Run discover schema for a given source a source configuration

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceCoreConfig.from_dict(body)
    return web.Response(status=200)
