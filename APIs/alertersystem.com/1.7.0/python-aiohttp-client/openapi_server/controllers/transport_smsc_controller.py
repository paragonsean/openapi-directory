from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_smsc_get_collection200_response import ApiTransportSmscGetCollection200Response
from openapi_server.models.transport_smsc_get import TransportSmscGet
from openapi_server.models.transport_smsc_jsonld_get import TransportSmscJsonldGet
from openapi_server.models.transport_smsc_jsonld_post import TransportSmscJsonldPost
from openapi_server.models.transport_smsc_jsonld_put import TransportSmscJsonldPut
from openapi_server.models.transport_smsc_patch import TransportSmscPatch
from openapi_server.models.transport_smsc_post import TransportSmscPost
from openapi_server.models.transport_smsc_put import TransportSmscPut
from openapi_server import util


async def api_transport_smsc_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSmsc resources.

    Retrieves the collection of TransportSmsc resources.

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


async def api_transport_smsc_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSmsc resource.

    Removes the TransportSmsc resource.

    :param id: TransportSmsc identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsc_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSmsc resource.

    Retrieves a TransportSmsc resource.

    :param id: TransportSmsc identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsc_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSmsc resource.

    Updates the TransportSmsc resource.

    :param id: TransportSmsc identifier
    :type id: str
    :param body: The updated TransportSmsc resource
    :type body: dict | bytes

    """
    body = TransportSmscPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsc_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSmsc resource.

    Replaces the TransportSmsc resource.

    :param id: TransportSmsc identifier
    :type id: str
    :param body: The updated TransportSmsc resource
    :type body: dict | bytes

    """
    body = TransportSmscPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsc_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSmsc resource.

    Creates a TransportSmsc resource.

    :param body: The new TransportSmsc resource
    :type body: dict | bytes

    """
    body = TransportSmscPost.from_dict(body)
    return web.Response(status=200)
