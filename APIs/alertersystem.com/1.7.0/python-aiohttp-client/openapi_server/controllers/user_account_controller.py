from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_user_account_get_collection200_response import ApiUserAccountGetCollection200Response
from openapi_server.models.user_account_get import UserAccountGet
from openapi_server.models.user_account_jsonld_get import UserAccountJsonldGet
from openapi_server.models.user_account_jsonld_put import UserAccountJsonldPut
from openapi_server.models.user_account_patch import UserAccountPatch
from openapi_server.models.user_account_put import UserAccountPut
from openapi_server import util


async def api_user_account_get_collection(request: web.Request, page=None, properties=None) -> web.Response:
    """Retrieves the collection of UserAccount resources.

    Retrieves the collection of UserAccount resources.

    :param page: The collection page number
    :type page: int
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_user_account_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a UserAccount resource.

    Retrieves a UserAccount resource.

    :param id: UserAccount identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_user_account_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the UserAccount resource.

    Updates the UserAccount resource.

    :param id: UserAccount identifier
    :type id: str
    :param body: The updated UserAccount resource
    :type body: dict | bytes

    """
    body = UserAccountPatch.from_dict(body)
    return web.Response(status=200)


async def api_user_account_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the UserAccount resource.

    Replaces the UserAccount resource.

    :param id: UserAccount identifier
    :type id: str
    :param body: The updated UserAccount resource
    :type body: dict | bytes

    """
    body = UserAccountPut.from_dict(body)
    return web.Response(status=200)
