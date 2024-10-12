from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_click_send_get_collection200_response import ApiTransportClickSendGetCollection200Response
from openapi_server.models.transport_click_send_get import TransportClickSendGet
from openapi_server.models.transport_click_send_jsonld_get import TransportClickSendJsonldGet
from openapi_server.models.transport_click_send_jsonld_post import TransportClickSendJsonldPost
from openapi_server.models.transport_click_send_jsonld_put import TransportClickSendJsonldPut
from openapi_server.models.transport_click_send_patch import TransportClickSendPatch
from openapi_server.models.transport_click_send_post import TransportClickSendPost
from openapi_server.models.transport_click_send_put import TransportClickSendPut
from openapi_server import util


async def api_transport_click_send_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportClickSend resources.

    Retrieves the collection of TransportClickSend resources.

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


async def api_transport_click_send_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportClickSend resource.

    Removes the TransportClickSend resource.

    :param id: TransportClickSend identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_click_send_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportClickSend resource.

    Retrieves a TransportClickSend resource.

    :param id: TransportClickSend identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_click_send_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportClickSend resource.

    Updates the TransportClickSend resource.

    :param id: TransportClickSend identifier
    :type id: str
    :param body: The updated TransportClickSend resource
    :type body: dict | bytes

    """
    body = TransportClickSendPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_click_send_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportClickSend resource.

    Replaces the TransportClickSend resource.

    :param id: TransportClickSend identifier
    :type id: str
    :param body: The updated TransportClickSend resource
    :type body: dict | bytes

    """
    body = TransportClickSendPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_click_send_post(request: web.Request, body) -> web.Response:
    """Creates a TransportClickSend resource.

    Creates a TransportClickSend resource.

    :param body: The new TransportClickSend resource
    :type body: dict | bytes

    """
    body = TransportClickSendPost.from_dict(body)
    return web.Response(status=200)
