from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_environment_response import ListEnvironmentResponse
from openapi_server.models.serverless_v1_service_environment import ServerlessV1ServiceEnvironment
from openapi_server import util


async def create_environment(request: web.Request, service_sid, unique_name, domain_suffix=None) -> web.Response:
    """create_environment

    Create a new environment.

    :param service_sid: The SID of the Service to create the Environment resource under.
    :type service_sid: str
    :param unique_name: A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters.
    :type unique_name: str
    :param domain_suffix: A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters.
    :type domain_suffix: str

    """
    return web.Response(status=200)


async def delete_environment(request: web.Request, service_sid, sid) -> web.Response:
    """delete_environment

    Delete a specific environment.

    :param service_sid: The SID of the Service to delete the Environment resource from.
    :type service_sid: str
    :param sid: The SID of the Environment resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_environment(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_environment

    Retrieve a specific environment.

    :param service_sid: The SID of the Service to fetch the Environment resource from.
    :type service_sid: str
    :param sid: The SID of the Environment resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_environment(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_environment

    Retrieve a list of all environments.

    :param service_sid: The SID of the Service to read the Environment resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
