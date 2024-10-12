from typing import List, Dict
from aiohttp import web

from openapi_server.models.article_index import ArticleIndex
from openapi_server.models.organization import Organization
from openapi_server.models.user import User
from openapi_server import util


async def get_org_articles(request: web.Request, username, page=None, per_page=None) -> web.Response:
    """Organization&#39;s Articles

    This endpoint allows the client to retrieve a list of Articles belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

    :param username: 
    :type username: str
    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_org_users(request: web.Request, username, page=None, per_page=None) -> web.Response:
    """Organization&#39;s users

    This endpoint allows the client to retrieve a list of users belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

    :param username: 
    :type username: str
    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_organization(request: web.Request, username) -> web.Response:
    """An organization

    This endpoint allows the client to retrieve a single organization by their username

    :param username: 
    :type username: str

    """
    return web.Response(status=200)
