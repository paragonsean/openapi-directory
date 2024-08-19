from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def keywords_delete_user_keyword(request: web.Request, user_guid, guid) -> web.Response:
    """Delete a keyword from the user

    Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

    :param user_guid: 
    :type user_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_values_delete_user_custom_value(request: web.Request, guid) -> web.Response:
    """Deletes a user custom value.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the user custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def users_delete_user(request: web.Request, guid) -> web.Response:
    """Delete an user.

    No Content (204) if succeeded. Bad Request (400) if user can&#39;t be deleted. Not Found (404) if the user can&#39;t be found.

    :param guid: ID of the user.
    :type guid: str

    """
    return web.Response(status=200)


async def work_contracts_delete_work_contract_0(request: web.Request, guid) -> web.Response:
    """Delete a work contract.

    Returns: No Content (204) if succeeded. Not found (404) if work contract can&#39;t be found.

    :param guid: ID for the work contract to delete.
    :type guid: str

    """
    return web.Response(status=200)
