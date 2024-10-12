from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_log_status_code_get import AlertLogStatusCodeGet
from openapi_server.models.alert_log_status_code_jsonld_get import AlertLogStatusCodeJsonldGet
from openapi_server.models.api_alert_log_status_code_get_collection200_response import ApiAlertLogStatusCodeGetCollection200Response
from openapi_server import util


async def api_alert_log_status_code_get_collection(request: web.Request, page=None, properties=None) -> web.Response:
    """Retrieves the collection of AlertLogStatusCode resources.

    Retrieves the collection of AlertLogStatusCode resources.

    :param page: The collection page number
    :type page: int
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_alert_log_status_code_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a AlertLogStatusCode resource.

    Retrieves a AlertLogStatusCode resource.

    :param id: AlertLogStatusCode identifier
    :type id: str

    """
    return web.Response(status=200)
