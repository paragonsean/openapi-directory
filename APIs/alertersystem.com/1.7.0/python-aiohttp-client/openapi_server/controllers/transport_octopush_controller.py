from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_octopush_get_collection200_response import ApiTransportOctopushGetCollection200Response
from openapi_server.models.transport_octopush_get import TransportOctopushGet
from openapi_server.models.transport_octopush_jsonld_get import TransportOctopushJsonldGet
from openapi_server.models.transport_octopush_jsonld_post import TransportOctopushJsonldPost
from openapi_server.models.transport_octopush_jsonld_put import TransportOctopushJsonldPut
from openapi_server.models.transport_octopush_patch import TransportOctopushPatch
from openapi_server.models.transport_octopush_post import TransportOctopushPost
from openapi_server.models.transport_octopush_put import TransportOctopushPut
from openapi_server import util


async def api_transport_octopush_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportOctopush resources.

    Retrieves the collection of TransportOctopush resources.

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


async def api_transport_octopush_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportOctopush resource.

    Removes the TransportOctopush resource.

    :param id: TransportOctopush identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_octopush_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportOctopush resource.

    Retrieves a TransportOctopush resource.

    :param id: TransportOctopush identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_octopush_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportOctopush resource.

    Updates the TransportOctopush resource.

    :param id: TransportOctopush identifier
    :type id: str
    :param body: The updated TransportOctopush resource
    :type body: dict | bytes

    """
    body = TransportOctopushPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_octopush_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportOctopush resource.

    Replaces the TransportOctopush resource.

    :param id: TransportOctopush identifier
    :type id: str
    :param body: The updated TransportOctopush resource
    :type body: dict | bytes

    """
    body = TransportOctopushPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_octopush_post(request: web.Request, body) -> web.Response:
    """Creates a TransportOctopush resource.

    Creates a TransportOctopush resource.

    :param body: The new TransportOctopush resource
    :type body: dict | bytes

    """
    body = TransportOctopushPost.from_dict(body)
    return web.Response(status=200)
