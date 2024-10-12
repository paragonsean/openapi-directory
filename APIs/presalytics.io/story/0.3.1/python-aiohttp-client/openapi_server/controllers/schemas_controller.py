from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def story_outline_schema(request: web.Request, schema_version) -> web.Response:
    """Story Outline Schema

    Json Schema for validating Story Outline objects

    :param schema_version: The semanitic version of a schema (e.g. &#39;0.3.1&#39;)
    :type schema_version: str

    """
    return web.Response(status=200)
