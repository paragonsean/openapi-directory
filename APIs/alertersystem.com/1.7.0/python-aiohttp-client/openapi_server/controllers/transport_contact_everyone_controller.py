from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_contact_everyone_get_collection200_response import ApiTransportContactEveryoneGetCollection200Response
from openapi_server.models.transport_contact_everyone_get import TransportContactEveryoneGet
from openapi_server.models.transport_contact_everyone_jsonld_get import TransportContactEveryoneJsonldGet
from openapi_server.models.transport_contact_everyone_jsonld_post import TransportContactEveryoneJsonldPost
from openapi_server.models.transport_contact_everyone_jsonld_put import TransportContactEveryoneJsonldPut
from openapi_server.models.transport_contact_everyone_patch import TransportContactEveryonePatch
from openapi_server.models.transport_contact_everyone_post import TransportContactEveryonePost
from openapi_server.models.transport_contact_everyone_put import TransportContactEveryonePut
from openapi_server import util


async def api_transport_contact_everyone_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportContactEveryone resources.

    Retrieves the collection of TransportContactEveryone resources.

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


async def api_transport_contact_everyone_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportContactEveryone resource.

    Removes the TransportContactEveryone resource.

    :param id: TransportContactEveryone identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_contact_everyone_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportContactEveryone resource.

    Retrieves a TransportContactEveryone resource.

    :param id: TransportContactEveryone identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_contact_everyone_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportContactEveryone resource.

    Updates the TransportContactEveryone resource.

    :param id: TransportContactEveryone identifier
    :type id: str
    :param body: The updated TransportContactEveryone resource
    :type body: dict | bytes

    """
    body = TransportContactEveryonePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_contact_everyone_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportContactEveryone resource.

    Replaces the TransportContactEveryone resource.

    :param id: TransportContactEveryone identifier
    :type id: str
    :param body: The updated TransportContactEveryone resource
    :type body: dict | bytes

    """
    body = TransportContactEveryonePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_contact_everyone_post(request: web.Request, body) -> web.Response:
    """Creates a TransportContactEveryone resource.

    Creates a TransportContactEveryone resource.

    :param body: The new TransportContactEveryone resource
    :type body: dict | bytes

    """
    body = TransportContactEveryonePost.from_dict(body)
    return web.Response(status=200)
