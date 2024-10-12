from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts import Accounts
from openapi_server.models.users import Users
from openapi_server import util


async def delete_user(request: web.Request, serverid, userid) -> web.Response:
    """Delete a specific user

    Delete a user. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)


async def delete_user_accounts(request: web.Request, serverid, userid) -> web.Response:
    """Delete all accounts of a specific user

    Delete all accounts corresponding to this user. The user itself is not deleted. Required permission: &#39;accounts&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)


async def delete_user_attribute(request: web.Request, serverid, userid, attributekey) -> web.Response:
    """Delete specific attribute of a specific user

    Delete attribute with the specified key of a specific user. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str
    :param attributekey: Key of the attribute
    :type attributekey: str

    """
    return web.Response(status=200)


async def delete_user_attributes(request: web.Request, serverid, userid) -> web.Response:
    """Delete all attributes of a specific user

    Delete all attributes of a specific user. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, serverid, userid, limit=None, marker=None, sort=None) -> web.Response:
    """Get all accounts of a specific user

    Returns an array containing all accounts corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str
    :param limit: Limit the number of results
    :type limit: int
    :param marker: Offset in the result list
    :type marker: int
    :param sort: Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    :type sort: str

    """
    return web.Response(status=200)


async def get_user_attributes(request: web.Request, serverid, userid) -> web.Response:
    """Get all attributes of a specific user

    Returns an array containing all attributes corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, serverid, filter=None, search=None, limit=None, marker=None, sort=None) -> web.Response:
    """Get all users

    Returns an array of arrays containing all accounts corresponding to all users. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param filter: Filter users based on an attribute. Takes the format *attributename&#x3D;attributevalue*. You can filter for multiple values at once, e.g. *group&#x3D;in:group1,group2*
    :type filter: str
    :param search: Search for a username LIKE %search%
    :type search: str
    :param limit: Limit the number of results
    :type limit: int
    :param marker: Offset in the result list
    :type marker: int
    :param sort: Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    :type sort: str

    """
    return web.Response(status=200)


async def register_user(request: web.Request, serverid, x_nonce, userid) -> web.Response:
    """Register a userid for the currently logged in account.

    Register a user for the currently logged in account. You can also directly pass a user name when generating an ENROL qr code. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param userid: Username to register
    :type userid: str

    """
    return web.Response(status=200)


async def set_user_attributes(request: web.Request, serverid, userid, attributes) -> web.Response:
    """Set all attributes of a specific user

    Set the attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will be deleted. Creates the user if not exists. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str
    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)


async def update_user_attributes(request: web.Request, serverid, userid, attributes) -> web.Response:
    """Update specified attributes of a specific user

    Update the specified attributes of a specific user. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str
    :param attributes: Array of attributes
    :type attributes: 

    """
    return web.Response(status=200)
