from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_my_sql_database import CreateMySqlDatabase
from openapi_server.models.create_my_sql_user import CreateMySqlUser
from openapi_server.models.my_sql_database import MySqlDatabase
from openapi_server.models.my_sql_user import MySqlUser
from openapi_server.models.update_user_password_request import UpdateUserPasswordRequest
from openapi_server.models.update_user_status_request import UpdateUserStatusRequest
from openapi_server import util


async def change_database_user_password(request: web.Request, database_name, user_name, database_name2, user_name2, body=None) -> web.Response:
    """Change password for mysql user

    

    :param database_name: Name of the database.
    :type database_name: str
    :param user_name: Name of the user.
    :type user_name: str
    :param database_name2: Automatically added
    :type database_name2: str
    :param user_name2: Automatically added
    :type user_name2: str
    :param body: Contains the new password.
    :type body: dict | bytes

    """
    body = UpdateUserPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def change_database_user_status(request: web.Request, database_name, user_name, database_name2, user_name2, body=None) -> web.Response:
    """Enable/disable mysql user

    

    :param database_name: Name of the database.
    :type database_name: str
    :param user_name: Name of the user.
    :type user_name: str
    :param database_name2: Automatically added
    :type database_name2: str
    :param user_name2: Automatically added
    :type user_name2: str
    :param body: Whether the user is enabled or not.
    :type body: dict | bytes

    """
    body = UpdateUserStatusRequest.from_dict(body)
    return web.Response(status=200)


async def create_my_sql_database(request: web.Request, body=None) -> web.Response:
    """Create a new mysql database

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateMySqlDatabase.from_dict(body)
    return web.Response(status=200)


async def create_my_sql_user(request: web.Request, database_name, database_name2, body=None) -> web.Response:
    """Create a new mysql user

    The creation of a new mysql user will result in a user with read_only rights.

    :param database_name: Name of the database.
    :type database_name: str
    :param database_name2: Automatically added
    :type database_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMySqlUser.from_dict(body)
    return web.Response(status=200)


async def delete_database(request: web.Request, database_name, database_name2) -> web.Response:
    """Delete a mysql database

    

    :param database_name: Name of the database.
    :type database_name: str
    :param database_name2: Automatically added
    :type database_name2: str

    """
    return web.Response(status=200)


async def delete_database_user(request: web.Request, database_name, user_name, database_name2, user_name2) -> web.Response:
    """Delete a mysql user

    The deletion of a mysql user is allowed for users with read_only rights.

    :param database_name: Name of the database.
    :type database_name: str
    :param user_name: Name of the user.
    :type user_name: str
    :param database_name2: Automatically added
    :type database_name2: str
    :param user_name2: Automatically added
    :type user_name2: str

    """
    return web.Response(status=200)


async def get_database_users(request: web.Request, database_name, database_name2) -> web.Response:
    """Overview of mysql users

    

    :param database_name: Name of the database.
    :type database_name: str
    :param database_name2: Automatically added
    :type database_name2: str

    """
    return web.Response(status=200)


async def get_my_sql_database(request: web.Request, database_name, database_name2) -> web.Response:
    """Get a specific database

    

    :param database_name: 
    :type database_name: str
    :param database_name2: Automatically added
    :type database_name2: str

    """
    return web.Response(status=200)


async def get_my_sql_databases(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of mysql databases

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)
