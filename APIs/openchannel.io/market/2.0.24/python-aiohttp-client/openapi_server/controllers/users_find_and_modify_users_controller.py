from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_pages import UserPages
from openapi_server import util


async def users_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of users

    - Results are paginated and the default is value is 100 if no limit is provided 

    :param query: A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the users that have the name &#39;John&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def users_user_id_delete(request: web.Request, user_id) -> web.Response:
    """Removes a single user

    - Results are returned for the market provided within the basic authentication credentials 

    :param user_id: The id of the user to be removed
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_get(request: web.Request, user_id) -> web.Response:
    """Return a single user

    - Results are returned for the market provided within the basic authentication credentials 

    :param user_id: The id of the user to be located
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_patch(request: web.Request, user_id, type=None, email=None, username=None, name=None, custom_data=None) -> web.Response:
    """Updates user fields

    

    :param user_id: The id of the user to be updated
    :type user_id: str
    :param type: The type for this user
    :type type: str
    :param email: The user&#39;s email
    :type email: str
    :param username: The user&#39;s username
    :type username: str
    :param name: The user&#39;s name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def users_user_id_post(request: web.Request, user_id, type=None, email=None, username=None, name=None, custom_data=None) -> web.Response:
    """Updates a single user or adds the user if they don&#39;t exist

    

    :param user_id: The id of the user to be updated
    :type user_id: str
    :param type: The type for this user
    :type type: str
    :param email: The user&#39;s email
    :type email: str
    :param username: The user&#39;s username
    :type username: str
    :param name: The user&#39;s name
    :type name: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)
