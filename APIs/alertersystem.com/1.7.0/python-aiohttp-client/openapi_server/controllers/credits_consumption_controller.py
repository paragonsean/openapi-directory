from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_credits_consumption_get_collection200_response import ApiCreditsConsumptionGetCollection200Response
from openapi_server.models.credits_consumption_get import CreditsConsumptionGet
from openapi_server.models.credits_consumption_jsonld_get import CreditsConsumptionJsonldGet
from openapi_server import util


async def api_credits_consumption_get_collection(request: web.Request, page=None, properties=None) -> web.Response:
    """Retrieves the collection of CreditsConsumption resources.

    Retrieves the collection of CreditsConsumption resources.

    :param page: The collection page number
    :type page: int
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_credits_consumption_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a CreditsConsumption resource.

    Retrieves a CreditsConsumption resource.

    :param id: CreditsConsumption identifier
    :type id: str

    """
    return web.Response(status=200)
