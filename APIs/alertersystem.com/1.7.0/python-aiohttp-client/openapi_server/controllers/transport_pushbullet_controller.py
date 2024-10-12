from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_pushbullet_get_collection200_response import ApiTransportPushbulletGetCollection200Response
from openapi_server.models.transport_pushbullet_get import TransportPushbulletGet
from openapi_server.models.transport_pushbullet_jsonld_get import TransportPushbulletJsonldGet
from openapi_server.models.transport_pushbullet_jsonld_post import TransportPushbulletJsonldPost
from openapi_server.models.transport_pushbullet_jsonld_put import TransportPushbulletJsonldPut
from openapi_server.models.transport_pushbullet_patch import TransportPushbulletPatch
from openapi_server.models.transport_pushbullet_post import TransportPushbulletPost
from openapi_server.models.transport_pushbullet_put import TransportPushbulletPut
from openapi_server import util


async def api_transport_pushbullet_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportPushbullet resources.

    Retrieves the collection of TransportPushbullet resources.

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


async def api_transport_pushbullet_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportPushbullet resource.

    Removes the TransportPushbullet resource.

    :param id: TransportPushbullet identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pushbullet_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportPushbullet resource.

    Retrieves a TransportPushbullet resource.

    :param id: TransportPushbullet identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pushbullet_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportPushbullet resource.

    Updates the TransportPushbullet resource.

    :param id: TransportPushbullet identifier
    :type id: str
    :param body: The updated TransportPushbullet resource
    :type body: dict | bytes

    """
    body = TransportPushbulletPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_pushbullet_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportPushbullet resource.

    Replaces the TransportPushbullet resource.

    :param id: TransportPushbullet identifier
    :type id: str
    :param body: The updated TransportPushbullet resource
    :type body: dict | bytes

    """
    body = TransportPushbulletPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_pushbullet_post(request: web.Request, body) -> web.Response:
    """Creates a TransportPushbullet resource.

    Creates a TransportPushbullet resource.

    :param body: The new TransportPushbullet resource
    :type body: dict | bytes

    """
    body = TransportPushbulletPost.from_dict(body)
    return web.Response(status=200)
