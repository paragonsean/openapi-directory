from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_v3_ci_lint_request import PostV3CiLintRequest
from openapi_server import util


async def post_v3_ci_lint(request: web.Request, body) -> web.Response:
    """Validation of .gitlab-ci.yml content

    Validation of .gitlab-ci.yml content

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3CiLintRequest.from_dict(body)
    return web.Response(status=200)
