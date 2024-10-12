from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_pushy_get_collection200_response import ApiTransportPushyGetCollection200Response
from openapi_server.models.transport_pushy_get import TransportPushyGet
from openapi_server.models.transport_pushy_jsonld_get import TransportPushyJsonldGet
from openapi_server.models.transport_pushy_jsonld_post import TransportPushyJsonldPost
from openapi_server.models.transport_pushy_jsonld_put import TransportPushyJsonldPut
from openapi_server.models.transport_pushy_patch import TransportPushyPatch
from openapi_server.models.transport_pushy_post import TransportPushyPost
from openapi_server.models.transport_pushy_put import TransportPushyPut
from openapi_server import util


async def api_transport_pushy_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportPushy resources.

    Retrieves the collection of TransportPushy resources.

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


async def api_transport_pushy_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportPushy resource.

    Removes the TransportPushy resource.

    :param id: TransportPushy identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pushy_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportPushy resource.

    Retrieves a TransportPushy resource.

    :param id: TransportPushy identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pushy_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportPushy resource.

    Updates the TransportPushy resource.

    :param id: TransportPushy identifier
    :type id: str
    :param body: The updated TransportPushy resource
    :type body: dict | bytes

    """
    body = TransportPushyPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_pushy_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportPushy resource.

    Replaces the TransportPushy resource.

    :param id: TransportPushy identifier
    :type id: str
    :param body: The updated TransportPushy resource
    :type body: dict | bytes

    """
    body = TransportPushyPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_pushy_post(request: web.Request, body) -> web.Response:
    """Creates a TransportPushy resource.

    Creates a TransportPushy resource.

    :param body: The new TransportPushy resource
    :type body: dict | bytes

    """
    body = TransportPushyPost.from_dict(body)
    return web.Response(status=200)
