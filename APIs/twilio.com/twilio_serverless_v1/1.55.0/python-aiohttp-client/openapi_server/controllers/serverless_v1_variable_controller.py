from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_variable_response import ListVariableResponse
from openapi_server.models.serverless_v1_service_environment_variable import ServerlessV1ServiceEnvironmentVariable
from openapi_server import util


async def create_variable(request: web.Request, service_sid, environment_sid, key, value) -> web.Response:
    """create_variable

    Create a new Variable.

    :param service_sid: The SID of the Service to create the Variable resource under.
    :type service_sid: str
    :param environment_sid: The SID of the Environment in which the Variable resource exists.
    :type environment_sid: str
    :param key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
    :type key: str
    :param value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
    :type value: str

    """
    return web.Response(status=200)


async def delete_variable(request: web.Request, service_sid, environment_sid, sid) -> web.Response:
    """delete_variable

    Delete a specific Variable.

    :param service_sid: The SID of the Service to delete the Variable resource from.
    :type service_sid: str
    :param environment_sid: The SID of the Environment with the Variables to delete.
    :type environment_sid: str
    :param sid: The SID of the Variable resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_variable(request: web.Request, service_sid, environment_sid, sid) -> web.Response:
    """fetch_variable

    Retrieve a specific Variable.

    :param service_sid: The SID of the Service to fetch the Variable resource from.
    :type service_sid: str
    :param environment_sid: The SID of the Environment with the Variable resource to fetch.
    :type environment_sid: str
    :param sid: The SID of the Variable resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_variable(request: web.Request, service_sid, environment_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_variable

    Retrieve a list of all Variables.

    :param service_sid: The SID of the Service to read the Variable resources from.
    :type service_sid: str
    :param environment_sid: The SID of the Environment with the Variable resources to read.
    :type environment_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_variable(request: web.Request, service_sid, environment_sid, sid, key=None, value=None) -> web.Response:
    """update_variable

    Update a specific Variable.

    :param service_sid: The SID of the Service to update the Variable resource under.
    :type service_sid: str
    :param environment_sid: The SID of the Environment with the Variable resource to update.
    :type environment_sid: str
    :param sid: The SID of the Variable resource to update.
    :type sid: str
    :param key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
    :type key: str
    :param value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
    :type value: str

    """
    return web.Response(status=200)
