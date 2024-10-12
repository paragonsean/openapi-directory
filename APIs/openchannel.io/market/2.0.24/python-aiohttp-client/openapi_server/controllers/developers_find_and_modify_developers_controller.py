from typing import List, Dict
from aiohttp import web

from openapi_server.models.developer import Developer
from openapi_server.models.developer_pages import DeveloperPages
from openapi_server import util


async def developers_developer_id_delete(request: web.Request, developer_id) -> web.Response:
    """Removes a single developer

    

    :param developer_id: The id of the developer to be removed
    :type developer_id: str

    """
    return web.Response(status=200)


async def developers_developer_id_get(request: web.Request, developer_id) -> web.Response:
    """Returns a single developer

    

    :param developer_id: The id of the developer to be located
    :type developer_id: str

    """
    return web.Response(status=200)


async def developers_developer_id_patch(request: web.Request, developer_id, type=None, email=None, username=None, name=None, custom_data=None) -> web.Response:
    """Updates the developer fields

    

    :param developer_id: The id of the developer to be located
    :type developer_id: str
    :param type: The type for this developer
    :type type: str
    :param email: The developer&#39;s email
    :type email: str
    :param username: The developer&#39;s username
    :type username: str
    :param name: The developer&#39;s name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def developers_developer_id_post(request: web.Request, developer_id, type=None, email=None, username=None, name=None, custom_data=None) -> web.Response:
    """Updates the developer record or adds the developer if it doesn&#39;t exist

    

    :param developer_id: The id of the developer to be located
    :type developer_id: str
    :param type: The type for this developer
    :type type: str
    :param email: The developer&#39;s email
    :type email: str
    :param username: The developer&#39;s username
    :type username: str
    :param name: The developer&#39;s name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def developers_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of developers

    - Results are paginated and the default is value is 100 if no limit is provided 

    :param query: A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the developers that have the name &#39;John&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)
