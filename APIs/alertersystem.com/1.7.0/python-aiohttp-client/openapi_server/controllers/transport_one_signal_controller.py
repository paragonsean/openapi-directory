from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_one_signal_get_collection200_response import ApiTransportOneSignalGetCollection200Response
from openapi_server.models.transport_one_signal_get import TransportOneSignalGet
from openapi_server.models.transport_one_signal_jsonld_get import TransportOneSignalJsonldGet
from openapi_server.models.transport_one_signal_jsonld_post import TransportOneSignalJsonldPost
from openapi_server.models.transport_one_signal_jsonld_put import TransportOneSignalJsonldPut
from openapi_server.models.transport_one_signal_patch import TransportOneSignalPatch
from openapi_server.models.transport_one_signal_post import TransportOneSignalPost
from openapi_server.models.transport_one_signal_put import TransportOneSignalPut
from openapi_server import util


async def api_transport_one_signal_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportOneSignal resources.

    Retrieves the collection of TransportOneSignal resources.

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


async def api_transport_one_signal_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportOneSignal resource.

    Removes the TransportOneSignal resource.

    :param id: TransportOneSignal identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_one_signal_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportOneSignal resource.

    Retrieves a TransportOneSignal resource.

    :param id: TransportOneSignal identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_one_signal_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportOneSignal resource.

    Updates the TransportOneSignal resource.

    :param id: TransportOneSignal identifier
    :type id: str
    :param body: The updated TransportOneSignal resource
    :type body: dict | bytes

    """
    body = TransportOneSignalPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_one_signal_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportOneSignal resource.

    Replaces the TransportOneSignal resource.

    :param id: TransportOneSignal identifier
    :type id: str
    :param body: The updated TransportOneSignal resource
    :type body: dict | bytes

    """
    body = TransportOneSignalPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_one_signal_post(request: web.Request, body) -> web.Response:
    """Creates a TransportOneSignal resource.

    Creates a TransportOneSignal resource.

    :param body: The new TransportOneSignal resource
    :type body: dict | bytes

    """
    body = TransportOneSignalPost.from_dict(body)
    return web.Response(status=200)
