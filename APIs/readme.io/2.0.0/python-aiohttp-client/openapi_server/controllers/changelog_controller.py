from typing import List, Dict
from aiohttp import web

from openapi_server.models.changelog import Changelog
from openapi_server import util


async def create_changelog(request: web.Request, body) -> web.Response:
    """Create changelog

    Create a new changelog inside of this project

    :param body: Changelog object
    :type body: dict | bytes

    """
    body = Changelog.from_dict(body)
    return web.Response(status=200)


async def delete_changelog(request: web.Request, slug) -> web.Response:
    """Delete changelog

    Delete the changelog with this slug

    :param slug: Slug of changelog
    :type slug: str

    """
    return web.Response(status=200)


async def get_changelog(request: web.Request, slug) -> web.Response:
    """Get changelog

    Returns the changelog with this slug

    :param slug: Slug of changelog
    :type slug: str

    """
    return web.Response(status=200)


async def get_changelogs(request: web.Request, per_page=None, page=None) -> web.Response:
    """Get changelogs

    Returns a list of changelogs associated with the project API key

    :param per_page: Number of items to include in pagination (up to 100, defaults to 10)
    :type per_page: int
    :param page: Used to specify further pages (starts at 1)
    :type page: int

    """
    return web.Response(status=200)


async def update_changelog(request: web.Request, slug, body) -> web.Response:
    """Update changelog

    Update a changelog with this slug

    :param slug: Slug of changelog
    :type slug: str
    :param body: Changelog object
    :type body: dict | bytes

    """
    body = Changelog.from_dict(body)
    return web.Response(status=200)
