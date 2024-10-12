from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_collection import ErrorCollection
from openapi_server import util


async def get_valid_project_key(request: web.Request, key=None) -> web.Response:
    """Get valid project key

    Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.  **[Permissions](#permissions) required:** None.

    :param key: The project key.
    :type key: str

    """
    return web.Response(status=200)


async def get_valid_project_name(request: web.Request, name) -> web.Response:
    """Get valid project name

    Checks that a project name isn&#39;t in use. If the name isn&#39;t in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.  **[Permissions](#permissions) required:** None.

    :param name: The project name.
    :type name: str

    """
    return web.Response(status=200)


async def validate_project_key(request: web.Request, key=None) -> web.Response:
    """Validate project key

    Validates a project key by confirming the key is a valid string and not in use.  **[Permissions](#permissions) required:** None.

    :param key: The project key.
    :type key: str

    """
    return web.Response(status=200)
