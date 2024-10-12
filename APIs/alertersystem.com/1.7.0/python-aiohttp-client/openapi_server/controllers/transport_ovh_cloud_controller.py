from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_ovh_cloud_get_collection200_response import ApiTransportOvhCloudGetCollection200Response
from openapi_server.models.transport_ovh_cloud_get import TransportOvhCloudGet
from openapi_server.models.transport_ovh_cloud_jsonld_get import TransportOvhCloudJsonldGet
from openapi_server.models.transport_ovh_cloud_jsonld_post import TransportOvhCloudJsonldPost
from openapi_server.models.transport_ovh_cloud_jsonld_put import TransportOvhCloudJsonldPut
from openapi_server.models.transport_ovh_cloud_patch import TransportOvhCloudPatch
from openapi_server.models.transport_ovh_cloud_post import TransportOvhCloudPost
from openapi_server.models.transport_ovh_cloud_put import TransportOvhCloudPut
from openapi_server import util


async def api_transport_ovh_cloud_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportOvhCloud resources.

    Retrieves the collection of TransportOvhCloud resources.

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


async def api_transport_ovh_cloud_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportOvhCloud resource.

    Removes the TransportOvhCloud resource.

    :param id: TransportOvhCloud identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_ovh_cloud_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportOvhCloud resource.

    Retrieves a TransportOvhCloud resource.

    :param id: TransportOvhCloud identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_ovh_cloud_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportOvhCloud resource.

    Updates the TransportOvhCloud resource.

    :param id: TransportOvhCloud identifier
    :type id: str
    :param body: The updated TransportOvhCloud resource
    :type body: dict | bytes

    """
    body = TransportOvhCloudPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_ovh_cloud_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportOvhCloud resource.

    Replaces the TransportOvhCloud resource.

    :param id: TransportOvhCloud identifier
    :type id: str
    :param body: The updated TransportOvhCloud resource
    :type body: dict | bytes

    """
    body = TransportOvhCloudPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_ovh_cloud_post(request: web.Request, body) -> web.Response:
    """Creates a TransportOvhCloud resource.

    Creates a TransportOvhCloud resource.

    :param body: The new TransportOvhCloud resource
    :type body: dict | bytes

    """
    body = TransportOvhCloudPost.from_dict(body)
    return web.Response(status=200)
