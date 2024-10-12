from typing import List, Dict
from aiohttp import web

from openapi_server.models.version import Version
from openapi_server import util


async def create_version(request: web.Request, body) -> web.Response:
    """Create version

    Create a new version

    :param body: Version object
    :type body: dict | bytes

    """
    body = Version.from_dict(body)
    return web.Response(status=200)


async def delete_version(request: web.Request, version_id) -> web.Response:
    """Delete version

    Delete a version

    :param version_id: Semver version indentifier
    :type version_id: str

    """
    return web.Response(status=200)


async def get_version(request: web.Request, version_id) -> web.Response:
    """Get version

    Returns the version with this version ID

    :param version_id: Semver version indentifier
    :type version_id: str

    """
    return web.Response(status=200)


async def get_versions(request: web.Request, ) -> web.Response:
    """Get versions

    Retrieve a list of versions associated with a project API key


    """
    return web.Response(status=200)


async def update_version(request: web.Request, version_id, body) -> web.Response:
    """Update version

    Update an existing version

    :param version_id: Semver version indentifier
    :type version_id: str
    :param body: Version object
    :type body: dict | bytes

    """
    body = Version.from_dict(body)
    return web.Response(status=200)
