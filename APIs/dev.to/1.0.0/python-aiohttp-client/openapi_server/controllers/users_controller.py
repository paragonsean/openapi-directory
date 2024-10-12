from typing import List, Dict
from aiohttp import web

from openapi_server.models.article_index import ArticleIndex
from openapi_server.models.user import User
from openapi_server.models.user_invite_param import UserInviteParam
from openapi_server import util


async def get_org_users_0(request: web.Request, username, page=None, per_page=None) -> web.Response:
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


async def get_user(request: web.Request, id) -> web.Response:
    """A User

    This endpoint allows the client to retrieve a single user, either by id or by the user&#39;s username.  For complete documentation, see the v0 API docs: https://developers.forem.com/api/v0#tag/users/operation/getUser

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_user_all_articles_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s all articles

    This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  It will return both published and unpublished articles with pagination.  Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.  By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_articles_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s articles

    This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_me(request: web.Request, ) -> web.Response:
    """The authenticated user

    This endpoint allows the client to retrieve information about the authenticated user


    """
    return web.Response(status=200)


async def get_user_published_articles_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s published articles

    This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_unpublished_articles_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s unpublished articles

    This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Unpublished articles will be in reverse chronological creation order.  It will return unpublished articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def post_admin_users_create(request: web.Request, body=None) -> web.Response:
    """Invite a User

    This endpoint allows the client to trigger an invitation to the provided email address.          It requires a token from a user with &#x60;super_admin&#x60; privileges.

    :param body: 
    :type body: dict | bytes

    """
    body = UserInviteParam.from_dict(body)
    return web.Response(status=200)


async def suspend_user(request: web.Request, id) -> web.Response:
    """Suspend a User

    This endpoint allows the client to suspend a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user will be assigned the &#39;suspended&#39; role. Suspending a user will stop the user from posting new posts and comments. It doesn&#39;t delete any of the user&#39;s content, just prevents them from creating new content while suspended. Users are not notified of their suspension in the UI, so if you want them to know about this, you must notify them.

    :param id: The ID of the user to suspend.
    :type id: int

    """
    return web.Response(status=200)


async def unpublish_user(request: web.Request, id) -> web.Response:
    """Unpublish a User&#39;s Articles and Comments

    This endpoint allows the client to unpublish all of the articles and comments created by a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user&#39;s articles and comments will be unpublished and will no longer be visible to the public. They will remain in the database and will set back to draft status on the specified user&#39;s  dashboard. Any notifications associated with the specified user&#39;s articles and comments will be deleted.  Note this endpoint unpublishes articles and comments asychronously: it will return a 204 NO CONTENT status code immediately, but the articles and comments will not be unpublished until the request is completed on the server.

    :param id: The ID of the user to unpublish.
    :type id: int

    """
    return web.Response(status=200)
