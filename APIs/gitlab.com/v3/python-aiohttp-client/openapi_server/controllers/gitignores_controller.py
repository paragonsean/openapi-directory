from typing import List, Dict
from aiohttp import web

from openapi_server.models.template import Template
from openapi_server.models.templates_list import TemplatesList
from openapi_server import util


async def get_v3_gitignores(request: web.Request, ) -> web.Response:
    """Get the list of the available template

    This feature was introduced in GitLab 8.8. This endpoint is deprecated and will be removed in GitLab 9.0.


    """
    return web.Response(status=200)


async def get_v3_gitignores_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific template present in local filesystem

    This feature was introduced in GitLab 8.8. This endpoint is deprecated and will be removed in GitLab 9.0.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)
