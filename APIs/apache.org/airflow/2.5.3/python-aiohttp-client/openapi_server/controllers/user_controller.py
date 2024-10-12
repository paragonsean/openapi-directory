from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user import User
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_collection_item import UserCollectionItem
from openapi_server import util


async def delete_user(request: web.Request, username) -> web.Response:
    """Delete a user

    Delete a user with a specific username.  *New in version 2.2.0* 

    :param username: The username of the user.  *New in version 2.1.0* 
    :type username: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, username) -> web.Response:
    """Get a user

    Get a user with a specific username.  *New in version 2.1.0* 

    :param username: The username of the user.  *New in version 2.1.0* 
    :type username: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List users

    Get a list of users.  *New in version 2.1.0* 

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_user(request: web.Request, username, body, update_mask=None) -> web.Response:
    """Update a user

    Update fields for a user.  *New in version 2.2.0* 

    :param username: The username of the user.  *New in version 2.1.0* 
    :type username: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def post_user(request: web.Request, body) -> web.Response:
    """Create a user

    Create a new user with unique username and email.  *New in version 2.2.0* 

    :param body: 
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)
