from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def get_environment(request: web.Request, ) -> web.Response:
    """Environment: Get

    pass rendering metadata to the client-side scripts


    """
    return web.Response(status=200)


async def spec_no_tags(request: web.Request, ) -> web.Response:
    """Specification: No tags

    json-formatted version of this spec with the tags removed to help with codegen processes


    """
    return web.Response(status=200)
