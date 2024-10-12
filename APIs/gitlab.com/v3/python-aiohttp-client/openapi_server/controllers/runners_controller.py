from typing import List, Dict
from aiohttp import web

from openapi_server.models.put_v3_runners_id_request import PutV3RunnersIdRequest
from openapi_server.models.runner import Runner
from openapi_server.models.runner_details import RunnerDetails
from openapi_server import util


async def delete_v3_runners_id(request: web.Request, id) -> web.Response:
    """Remove a runner

    Remove a runner

    :param id: The ID of the runner
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_runners(request: web.Request, scope=None, page=None, per_page=None) -> web.Response:
    """Get runners available for user

    Get runners available for user

    :param scope: The scope of specific runners to show
    :type scope: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_runners_all(request: web.Request, scope=None, page=None, per_page=None) -> web.Response:
    """Get all runners - shared and specific

    Get all runners - shared and specific

    :param scope: The scope of specific runners to show
    :type scope: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_runners_id(request: web.Request, id) -> web.Response:
    """Get runner&#39;s details

    Get runner&#39;s details

    :param id: The ID of the runner
    :type id: int

    """
    return web.Response(status=200)


async def put_v3_runners_id(request: web.Request, id, body=None) -> web.Response:
    """Update runner&#39;s details

    Update runner&#39;s details

    :param id: The ID of the runner
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3RunnersIdRequest.from_dict(body)
    return web.Response(status=200)
