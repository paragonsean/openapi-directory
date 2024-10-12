from typing import List, Dict
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_index import ArticleIndex
from openapi_server.models.video_article import VideoArticle
from openapi_server import util


async def create_article(request: web.Request, body=None) -> web.Response:
    """Publish article

    This endpoint allows the client to create a new article.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

    :param body: 
    :type body: dict | bytes

    """
    body = Article.from_dict(body)
    return web.Response(status=200)


async def get_article_by_id(request: web.Request, id) -> web.Response:
    """Published article by id

    This endpoint allows the client to retrieve a single published article given its &#x60;id&#x60;.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_article_by_path(request: web.Request, username, slug) -> web.Response:
    """Published article by path

    This endpoint allows the client to retrieve a single published article given its &#x60;path&#x60;.

    :param username: 
    :type username: str
    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def get_articles(request: web.Request, page=None, per_page=None, tag=None, tags=None, tags_exclude=None, username=None, state=None, top=None, collection_id=None) -> web.Response:
    """Published articles

    This endpoint allows the client to retrieve a list of articles.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  By default it will return featured, published articles ordered by descending popularity.  It supports pagination, each page will contain &#x60;30&#x60; articles by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int
    :param tag: Using this parameter will retrieve articles that contain the requested tag. Articles will be ordered by descending popularity.This parameter can be used in conjuction with &#x60;top&#x60;.
    :type tag: str
    :param tags: Using this parameter will retrieve articles with any of the comma-separated tags. Articles will be ordered by descending popularity.
    :type tags: str
    :param tags_exclude: Using this parameter will retrieve articles that do _not_ contain _any_ of comma-separated tags. Articles will be ordered by descending popularity.
    :type tags_exclude: str
    :param username: Using this parameter will retrieve articles belonging             to a User or Organization ordered by descending publication date.             If &#x60;state&#x3D;all&#x60; the number of items returned will be &#x60;1000&#x60; instead of the default &#x60;30&#x60;.             This parameter can be used in conjuction with &#x60;state&#x60;.
    :type username: str
    :param state: Using this parameter will allow the client to check which articles are fresh or rising.             If &#x60;state&#x3D;fresh&#x60; the server will return fresh articles.             If &#x60;state&#x3D;rising&#x60; the server will return rising articles.             This param can be used in conjuction with &#x60;username&#x60;, only if set to &#x60;all&#x60;.
    :type state: str
    :param top: Using this parameter will allow the client to return the most popular articles in the last &#x60;N&#x60; days. &#x60;top&#x60; indicates the number of days since publication of the articles returned. This param can be used in conjuction with &#x60;tag&#x60;.
    :type top: int
    :param collection_id: Adding this will allow the client to return the list of articles belonging to the requested collection, ordered by ascending publication date.
    :type collection_id: int

    """
    return web.Response(status=200)


async def get_latest_articles(request: web.Request, page=None, per_page=None) -> web.Response:
    """Published articles sorted by published date

    This endpoint allows the client to retrieve a list of articles. ordered by descending publish date.  It supports pagination, each page will contain 30 articles by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_org_articles_0(request: web.Request, username, page=None, per_page=None) -> web.Response:
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


async def get_user_all_articles(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s all articles

    This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  It will return both published and unpublished articles with pagination.  Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.  By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_articles(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s articles

    This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_published_articles(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s published articles

    This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_user_unpublished_articles(request: web.Request, page=None, per_page=None) -> web.Response:
    """User&#39;s unpublished articles

    This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Unpublished articles will be in reverse chronological creation order.  It will return unpublished articles with pagination. By default a page will contain 30 articles.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)


async def unpublish_article(request: web.Request, id, note=None) -> web.Response:
    """Unpublish an article

    This endpoint allows the client to unpublish an article.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  The article will be unpublished and will no longer be visible to the public. It will remain in the database and will set back to draft status on the author&#39;s posts dashboard. Any notifications associated with the article will be deleted. Any comments on the article will remain.

    :param id: The ID of the article to unpublish.
    :type id: int
    :param note: Content for the note that&#39;s created along with unpublishing
    :type note: str

    """
    return web.Response(status=200)


async def update_article(request: web.Request, id, body=None) -> web.Response:
    """Update an article by id

    This endpoint allows the client to update an existing article.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

    :param id: The ID of the user to unpublish.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Article.from_dict(body)
    return web.Response(status=200)


async def videos_0(request: web.Request, page=None, per_page=None) -> web.Response:
    """Articles with a video

    This endpoint allows the client to retrieve a list of articles that are uploaded with a video.  It will only return published video articles ordered by descending popularity.  It supports pagination, each page will contain 24 articles by default.

    :param page: Pagination page
    :type page: int
    :param per_page: Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable.
    :type per_page: int

    """
    return web.Response(status=200)
