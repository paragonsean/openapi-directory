from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_monitor_get_collection200_response import ApiMonitorGetCollection200Response
from openapi_server.models.monitor_get import MonitorGet
from openapi_server.models.monitor_jsonld_get import MonitorJsonldGet
from openapi_server.models.monitor_jsonld_post import MonitorJsonldPost
from openapi_server.models.monitor_jsonld_put import MonitorJsonldPut
from openapi_server.models.monitor_patch import MonitorPatch
from openapi_server.models.monitor_post import MonitorPost
from openapi_server.models.monitor_put import MonitorPut
from openapi_server import util


async def api_monitor_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of Monitor resources.

    Retrieves the collection of Monitor resources.

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


async def api_monitor_id_delete(request: web.Request, id) -> web.Response:
    """Removes the Monitor resource.

    Removes the Monitor resource.

    :param id: Monitor identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_monitor_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a Monitor resource.

    Retrieves a Monitor resource.

    :param id: Monitor identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_monitor_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the Monitor resource.

    Updates the Monitor resource.

    :param id: Monitor identifier
    :type id: str
    :param body: The updated Monitor resource
    :type body: dict | bytes

    """
    body = MonitorPatch.from_dict(body)
    return web.Response(status=200)


async def api_monitor_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the Monitor resource.

    Replaces the Monitor resource.

    :param id: Monitor identifier
    :type id: str
    :param body: The updated Monitor resource
    :type body: dict | bytes

    """
    body = MonitorPut.from_dict(body)
    return web.Response(status=200)


async def api_monitor_post(request: web.Request, body) -> web.Response:
    """Creates a Monitor resource.

    Creates a Monitor resource.

    :param body: The new Monitor resource
    :type body: dict | bytes

    """
    body = MonitorPost.from_dict(body)
    return web.Response(status=200)
