from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_page import CustomPage
from openapi_server import util


async def create_custom_page(request: web.Request, body) -> web.Response:
    """Create custom page

    Create a new custom page inside of this project

    :param body: CustomPage object
    :type body: dict | bytes

    """
    body = CustomPage.from_dict(body)
    return web.Response(status=200)


async def delete_custom_page(request: web.Request, slug) -> web.Response:
    """Delete custom page

    Delete the custom page with this slug

    :param slug: Slug of custom page
    :type slug: str

    """
    return web.Response(status=200)


async def get_custom_page(request: web.Request, slug) -> web.Response:
    """Get custom page

    Returns the custom page with this slug

    :param slug: Slug of custom page
    :type slug: str

    """
    return web.Response(status=200)


async def get_custom_pages(request: web.Request, per_page=None, page=None) -> web.Response:
    """Get custom pages

    Returns a list of custom pages associated with the project API key

    :param per_page: Number of items to include in pagination (up to 100, defaults to 10)
    :type per_page: int
    :param page: Used to specify further pages (starts at 1)
    :type page: int

    """
    return web.Response(status=200)


async def update_custom_page(request: web.Request, slug, body) -> web.Response:
    """Update custom page

    Update a custom page with this slug

    :param slug: Slug of custom page
    :type slug: str
    :param body: CustomPage object
    :type body: dict | bytes

    """
    body = CustomPage.from_dict(body)
    return web.Response(status=200)
