from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.key_failure import KeyFailure
from openapi_server.models.signin import Signin
from openapi_server.models.signin_response import SigninResponse
from openapi_server.models.user_record import UserRecord
from openapi_server import util


async def signin_post(request: web.Request, body=None) -> web.Response:
    """signin_post

    Create a new signin record

    :param body: 
    :type body: dict | bytes

    """
    body = Signin.from_dict(body)
    return web.Response(status=200)


async def signin_signin_id_delete(request: web.Request, signin_id) -> web.Response:
    """Delete a signin record

    Delete a signin record       

    :param signin_id: The ID of the signin record to be deleted.
    :type signin_id: int

    """
    return web.Response(status=200)


async def signin_signin_id_get(request: web.Request, signin_id) -> web.Response:
    """Retrieve the information associated with a signin record

    Retrieve the information associated with a signin record 

    :param signin_id: The ID of the signin record to be retrieved.
    :type signin_id: int

    """
    return web.Response(status=200)


async def signin_signin_id_put(request: web.Request, signin_id, body=None) -> web.Response:
    """Update a signin record

    Update a signin record 

    :param signin_id: The ID of the signin record to be retrieved.
    :type signin_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Signin.from_dict(body)
    return web.Response(status=200)


async def signins_get(request: web.Request, less_than=None, return_count=None) -> web.Response:
    """Get signin info

    Returns a list of signin objects sorted by signin ID descending.

    :param less_than: Return signins with IDs less than this value.
    :type less_than: int
    :param return_count: Return this many objects
    :type return_count: int

    """
    return web.Response(status=200)
