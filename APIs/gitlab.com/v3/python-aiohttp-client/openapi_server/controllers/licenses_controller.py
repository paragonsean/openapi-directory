from typing import List, Dict
from aiohttp import web

from openapi_server.models.repo_license import RepoLicense
from openapi_server import util


async def get_v3_licenses(request: web.Request, popular=None) -> web.Response:
    """Get the list of the available license template

    This feature was introduced in GitLab 8.7. This endpoint is deprecated and will be removed in GitLab 9.0.

    :param popular: If passed, returns only popular licenses
    :type popular: bool

    """
    return web.Response(status=200)


async def get_v3_licenses_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific license

    This feature was introduced in GitLab 8.7. This endpoint is deprecated and will be removed in GitLab 9.0.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)
