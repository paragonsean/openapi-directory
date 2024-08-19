from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_pages import UserAccountPages
from openapi_server import util


async def user_accounts_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of userAccounts

    - Results are paginated and the default is value is 1000 if no limit is provided 

    :param query: A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the userAccounts that have the name &#39;NASA&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def user_accounts_user_account_id_delete(request: web.Request, user_account_id) -> web.Response:
    """Removes the user account

    

    :param user_account_id: The id of the user account to be removed
    :type user_account_id: str

    """
    return web.Response(status=200)


async def user_accounts_user_account_id_get(request: web.Request, user_account_id) -> web.Response:
    """Returns a single user account

    

    :param user_account_id: The id of the user account to be located
    :type user_account_id: str

    """
    return web.Response(status=200)


async def user_accounts_user_account_id_patch(request: web.Request, user_account_id, user_id, email=None, name=None, custom_data=None) -> web.Response:
    """Updates the user account fields

    

    :param user_account_id: The id of the user account to be updated
    :type user_account_id: str
    :param user_id: The Id of the user that this account belongs to
    :type user_id: str
    :param email: The contact email address
    :type email: str
    :param name: The user account name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def user_accounts_user_account_id_post(request: web.Request, user_account_id, user_id, email=None, name=None, custom_data=None) -> web.Response:
    """Updates the user account or adds the user account if it doesn&#39;t exist

    

    :param user_account_id: The id of the user account to be updated
    :type user_account_id: str
    :param user_id: The Id of the user that this account belongs to
    :type user_id: str
    :param email: The contact email address
    :type email: str
    :param name: The user account name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)
