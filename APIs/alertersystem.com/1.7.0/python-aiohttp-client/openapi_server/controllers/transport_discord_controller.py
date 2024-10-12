from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_discord_get_collection200_response import ApiTransportDiscordGetCollection200Response
from openapi_server.models.transport_discord_get import TransportDiscordGet
from openapi_server.models.transport_discord_jsonld_get import TransportDiscordJsonldGet
from openapi_server.models.transport_discord_jsonld_post import TransportDiscordJsonldPost
from openapi_server.models.transport_discord_jsonld_put import TransportDiscordJsonldPut
from openapi_server.models.transport_discord_patch import TransportDiscordPatch
from openapi_server.models.transport_discord_post import TransportDiscordPost
from openapi_server.models.transport_discord_put import TransportDiscordPut
from openapi_server import util


async def api_transport_discord_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportDiscord resources.

    Retrieves the collection of TransportDiscord resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_transport_discord_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportDiscord resource.

    Removes the TransportDiscord resource.

    :param id: TransportDiscord identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_discord_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportDiscord resource.

    Retrieves a TransportDiscord resource.

    :param id: TransportDiscord identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_discord_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportDiscord resource.

    Updates the TransportDiscord resource.

    :param id: TransportDiscord identifier
    :type id: str
    :param body: The updated TransportDiscord resource
    :type body: dict | bytes

    """
    body = TransportDiscordPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_discord_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportDiscord resource.

    Replaces the TransportDiscord resource.

    :param id: TransportDiscord identifier
    :type id: str
    :param body: The updated TransportDiscord resource
    :type body: dict | bytes

    """
    body = TransportDiscordPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_discord_post(request: web.Request, body) -> web.Response:
    """Creates a TransportDiscord resource.

    Creates a TransportDiscord resource.

    :param body: The new TransportDiscord resource
    :type body: dict | bytes

    """
    body = TransportDiscordPost.from_dict(body)
    return web.Response(status=200)
