from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_mattermost_get_collection200_response import ApiTransportMattermostGetCollection200Response
from openapi_server.models.transport_mattermost_get import TransportMattermostGet
from openapi_server.models.transport_mattermost_jsonld_get import TransportMattermostJsonldGet
from openapi_server.models.transport_mattermost_jsonld_post import TransportMattermostJsonldPost
from openapi_server.models.transport_mattermost_jsonld_put import TransportMattermostJsonldPut
from openapi_server.models.transport_mattermost_patch import TransportMattermostPatch
from openapi_server.models.transport_mattermost_post import TransportMattermostPost
from openapi_server.models.transport_mattermost_put import TransportMattermostPut
from openapi_server import util


async def api_transport_mattermost_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMattermost resources.

    Retrieves the collection of TransportMattermost resources.

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


async def api_transport_mattermost_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMattermost resource.

    Removes the TransportMattermost resource.

    :param id: TransportMattermost identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mattermost_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMattermost resource.

    Retrieves a TransportMattermost resource.

    :param id: TransportMattermost identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mattermost_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMattermost resource.

    Updates the TransportMattermost resource.

    :param id: TransportMattermost identifier
    :type id: str
    :param body: The updated TransportMattermost resource
    :type body: dict | bytes

    """
    body = TransportMattermostPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_mattermost_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMattermost resource.

    Replaces the TransportMattermost resource.

    :param id: TransportMattermost identifier
    :type id: str
    :param body: The updated TransportMattermost resource
    :type body: dict | bytes

    """
    body = TransportMattermostPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_mattermost_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMattermost resource.

    Creates a TransportMattermost resource.

    :param body: The new TransportMattermost resource
    :type body: dict | bytes

    """
    body = TransportMattermostPost.from_dict(body)
    return web.Response(status=200)
