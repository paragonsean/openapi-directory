from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_gitter_get_collection200_response import ApiTransportGitterGetCollection200Response
from openapi_server.models.transport_gitter_get import TransportGitterGet
from openapi_server.models.transport_gitter_jsonld_get import TransportGitterJsonldGet
from openapi_server.models.transport_gitter_jsonld_post import TransportGitterJsonldPost
from openapi_server.models.transport_gitter_jsonld_put import TransportGitterJsonldPut
from openapi_server.models.transport_gitter_patch import TransportGitterPatch
from openapi_server.models.transport_gitter_post import TransportGitterPost
from openapi_server.models.transport_gitter_put import TransportGitterPut
from openapi_server import util


async def api_transport_gitter_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportGitter resources.

    Retrieves the collection of TransportGitter resources.

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


async def api_transport_gitter_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportGitter resource.

    Removes the TransportGitter resource.

    :param id: TransportGitter identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gitter_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportGitter resource.

    Retrieves a TransportGitter resource.

    :param id: TransportGitter identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gitter_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportGitter resource.

    Updates the TransportGitter resource.

    :param id: TransportGitter identifier
    :type id: str
    :param body: The updated TransportGitter resource
    :type body: dict | bytes

    """
    body = TransportGitterPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_gitter_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportGitter resource.

    Replaces the TransportGitter resource.

    :param id: TransportGitter identifier
    :type id: str
    :param body: The updated TransportGitter resource
    :type body: dict | bytes

    """
    body = TransportGitterPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_gitter_post(request: web.Request, body) -> web.Response:
    """Creates a TransportGitter resource.

    Creates a TransportGitter resource.

    :param body: The new TransportGitter resource
    :type body: dict | bytes

    """
    body = TransportGitterPost.from_dict(body)
    return web.Response(status=200)
