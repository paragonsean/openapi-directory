from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_telegram_get_collection200_response import ApiTransportTelegramGetCollection200Response
from openapi_server.models.transport_telegram_get import TransportTelegramGet
from openapi_server.models.transport_telegram_jsonld_get import TransportTelegramJsonldGet
from openapi_server.models.transport_telegram_jsonld_post import TransportTelegramJsonldPost
from openapi_server.models.transport_telegram_jsonld_put import TransportTelegramJsonldPut
from openapi_server.models.transport_telegram_patch import TransportTelegramPatch
from openapi_server.models.transport_telegram_post import TransportTelegramPost
from openapi_server.models.transport_telegram_put import TransportTelegramPut
from openapi_server import util


async def api_transport_telegram_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTelegram resources.

    Retrieves the collection of TransportTelegram resources.

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


async def api_transport_telegram_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTelegram resource.

    Removes the TransportTelegram resource.

    :param id: TransportTelegram identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_telegram_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTelegram resource.

    Retrieves a TransportTelegram resource.

    :param id: TransportTelegram identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_telegram_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTelegram resource.

    Updates the TransportTelegram resource.

    :param id: TransportTelegram identifier
    :type id: str
    :param body: The updated TransportTelegram resource
    :type body: dict | bytes

    """
    body = TransportTelegramPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_telegram_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTelegram resource.

    Replaces the TransportTelegram resource.

    :param id: TransportTelegram identifier
    :type id: str
    :param body: The updated TransportTelegram resource
    :type body: dict | bytes

    """
    body = TransportTelegramPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_telegram_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTelegram resource.

    Creates a TransportTelegram resource.

    :param body: The new TransportTelegram resource
    :type body: dict | bytes

    """
    body = TransportTelegramPost.from_dict(body)
    return web.Response(status=200)
