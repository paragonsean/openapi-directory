from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_types_list_result import EventTypesListResult
from openapi_server.models.topic_type_info import TopicTypeInfo
from openapi_server.models.topic_types_list_result import TopicTypesListResult
from openapi_server import util


async def topic_types_get(request: web.Request, topic_type_name, api_version) -> web.Response:
    """Get a topic type

    Get information about a topic type

    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topic_types_list(request: web.Request, api_version) -> web.Response:
    """List topic types

    List all registered topic types

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topic_types_list_event_types(request: web.Request, topic_type_name, api_version) -> web.Response:
    """List event types

    List event types for a topic type

    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
