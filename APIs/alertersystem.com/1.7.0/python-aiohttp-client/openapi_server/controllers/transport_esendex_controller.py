from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_esendex_get_collection200_response import ApiTransportEsendexGetCollection200Response
from openapi_server.models.transport_esendex_get import TransportEsendexGet
from openapi_server.models.transport_esendex_jsonld_get import TransportEsendexJsonldGet
from openapi_server.models.transport_esendex_jsonld_post import TransportEsendexJsonldPost
from openapi_server.models.transport_esendex_jsonld_put import TransportEsendexJsonldPut
from openapi_server.models.transport_esendex_patch import TransportEsendexPatch
from openapi_server.models.transport_esendex_post import TransportEsendexPost
from openapi_server.models.transport_esendex_put import TransportEsendexPut
from openapi_server import util


async def api_transport_esendex_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportEsendex resources.

    Retrieves the collection of TransportEsendex resources.

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


async def api_transport_esendex_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportEsendex resource.

    Removes the TransportEsendex resource.

    :param id: TransportEsendex identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_esendex_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportEsendex resource.

    Retrieves a TransportEsendex resource.

    :param id: TransportEsendex identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_esendex_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportEsendex resource.

    Updates the TransportEsendex resource.

    :param id: TransportEsendex identifier
    :type id: str
    :param body: The updated TransportEsendex resource
    :type body: dict | bytes

    """
    body = TransportEsendexPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_esendex_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportEsendex resource.

    Replaces the TransportEsendex resource.

    :param id: TransportEsendex identifier
    :type id: str
    :param body: The updated TransportEsendex resource
    :type body: dict | bytes

    """
    body = TransportEsendexPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_esendex_post(request: web.Request, body) -> web.Response:
    """Creates a TransportEsendex resource.

    Creates a TransportEsendex resource.

    :param body: The new TransportEsendex resource
    :type body: dict | bytes

    """
    body = TransportEsendexPost.from_dict(body)
    return web.Response(status=200)
