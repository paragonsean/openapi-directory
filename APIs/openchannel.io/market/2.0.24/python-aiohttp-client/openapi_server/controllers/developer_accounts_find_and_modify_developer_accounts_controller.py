from typing import List, Dict
from aiohttp import web

from openapi_server.models.developer_account import DeveloperAccount
from openapi_server.models.developer_account_pages import DeveloperAccountPages
from openapi_server import util


async def developer_accounts_developer_account_id_delete(request: web.Request, developer_account_id) -> web.Response:
    """Removes the developer account

    

    :param developer_account_id: The id of the developer account to be updated
    :type developer_account_id: str

    """
    return web.Response(status=200)


async def developer_accounts_developer_account_id_get(request: web.Request, developer_account_id) -> web.Response:
    """Returns a single developer account

    

    :param developer_account_id: The id of the developer account to be located
    :type developer_account_id: str

    """
    return web.Response(status=200)


async def developer_accounts_developer_account_id_patch(request: web.Request, developer_account_id, developer_id, email=None, name=None, custom_data=None) -> web.Response:
    """Updates the developer account fields

    

    :param developer_account_id: The id of the developer account to be updated
    :type developer_account_id: str
    :param developer_id: The id of the developer that this account belongs to
    :type developer_id: str
    :param email: The contact email address
    :type email: str
    :param name: The name for the account
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def developer_accounts_developer_account_id_post(request: web.Request, developer_account_id, developer_id, email=None, name=None, custom_data=None) -> web.Response:
    """Updates the developer account or adds the developer account if it doesn&#39;t exist

    

    :param developer_account_id: The id of the developer account to be updated
    :type developer_account_id: str
    :param developer_id: The id of the developer that this account belongs to
    :type developer_id: str
    :param email: The contact email address
    :type email: str
    :param name: The name for the account
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def developer_accounts_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of developerAccounts

    - Results are paginated and the default is value is 1000 if no limit is provided 

    :param query: A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the developerAccounts that have the name &#39;NASA&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)
