from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_firebase_get_collection200_response import ApiTransportFirebaseGetCollection200Response
from openapi_server.models.transport_firebase_get import TransportFirebaseGet
from openapi_server.models.transport_firebase_jsonld_get import TransportFirebaseJsonldGet
from openapi_server.models.transport_firebase_jsonld_post import TransportFirebaseJsonldPost
from openapi_server.models.transport_firebase_jsonld_put import TransportFirebaseJsonldPut
from openapi_server.models.transport_firebase_patch import TransportFirebasePatch
from openapi_server.models.transport_firebase_post import TransportFirebasePost
from openapi_server.models.transport_firebase_put import TransportFirebasePut
from openapi_server import util


async def api_transport_firebase_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportFirebase resources.

    Retrieves the collection of TransportFirebase resources.

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


async def api_transport_firebase_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportFirebase resource.

    Removes the TransportFirebase resource.

    :param id: TransportFirebase identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_firebase_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportFirebase resource.

    Retrieves a TransportFirebase resource.

    :param id: TransportFirebase identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_firebase_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportFirebase resource.

    Updates the TransportFirebase resource.

    :param id: TransportFirebase identifier
    :type id: str
    :param body: The updated TransportFirebase resource
    :type body: dict | bytes

    """
    body = TransportFirebasePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_firebase_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportFirebase resource.

    Replaces the TransportFirebase resource.

    :param id: TransportFirebase identifier
    :type id: str
    :param body: The updated TransportFirebase resource
    :type body: dict | bytes

    """
    body = TransportFirebasePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_firebase_post(request: web.Request, body) -> web.Response:
    """Creates a TransportFirebase resource.

    Creates a TransportFirebase resource.

    :param body: The new TransportFirebase resource
    :type body: dict | bytes

    """
    body = TransportFirebasePost.from_dict(body)
    return web.Response(status=200)
