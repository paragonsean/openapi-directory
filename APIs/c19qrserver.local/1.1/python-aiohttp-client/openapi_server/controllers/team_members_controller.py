from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.sample3 import Sample3
from openapi_server.models.user_record import UserRecord
from openapi_server import util


async def user_post(request: web.Request, body) -> web.Response:
    """Create a user

    Use this endpoint to create a team member (user) record

    :param body: Create User Payload
    :type body: dict | bytes

    """
    body = Sample3.from_dict(body)
    return web.Response(status=200)


async def user_user_id_delete(request: web.Request, user_id) -> web.Response:
    """Delete a team member&#39;s user record

    To preserve referential integrity in the database, the user account  will not be deleted from the database. Rather, the password will be set to the empty string, effectively preventing that user from logging in. Furthermore, all active sessions for that user will be deleted, as will any password reset tokens.  

    :param user_id: The ID of the user record to be deleted.
    :type user_id: int

    """
    return web.Response(status=200)


async def user_user_id_get(request: web.Request, user_id) -> web.Response:
    """Retrieve the information associated with a team member&#39;s user record

    Retrieve the information associated with a user&#39;s account 

    :param user_id: The ID of the user record to be retrieved.
    :type user_id: int

    """
    return web.Response(status=200)


async def users_get(request: web.Request, ) -> web.Response:
    """Retrieve the information associated with all team members&#39; user records

    Retrieve the information associated with all team members&#39; user records 


    """
    return web.Response(status=200)
