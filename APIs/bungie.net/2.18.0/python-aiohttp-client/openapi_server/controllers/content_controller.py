from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_get_content_by_id200_response import ContentGetContentById200Response
from openapi_server.models.content_get_content_type200_response import ContentGetContentType200Response
from openapi_server.models.content_rss_news_articles200_response import ContentRssNewsArticles200Response
from openapi_server.models.content_search_content_with_text200_response import ContentSearchContentWithText200Response
from openapi_server.models.content_search_help_articles200_response import ContentSearchHelpArticles200Response
from openapi_server import util


async def content_get_content_by_id(request: web.Request, id, locale, head=None) -> web.Response:
    """content_get_content_by_id

    Returns a content item referenced by id

    :param id: 
    :type id: int
    :param locale: 
    :type locale: str
    :param head: false
    :type head: bool

    """
    return web.Response(status=200)


async def content_get_content_by_tag_and_type(request: web.Request, locale, tag, type, head=None) -> web.Response:
    """content_get_content_by_tag_and_type

    Returns the newest item that matches a given tag and Content Type.

    :param locale: 
    :type locale: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param head: Not used.
    :type head: bool

    """
    return web.Response(status=200)


async def content_get_content_type(request: web.Request, type) -> web.Response:
    """content_get_content_type

    Gets an object describing a particular variant of content.

    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def content_rss_news_articles(request: web.Request, page_token, categoryfilter=None, includebody=None) -> web.Response:
    """content_rss_news_articles

    Returns a JSON string response that is the RSS feed for news articles.

    :param page_token: Zero-based pagination token for paging through result sets.
    :type page_token: str
    :param categoryfilter: Optionally filter response to only include news items in a certain category.
    :type categoryfilter: str
    :param includebody: Optionally include full content body for each news item.
    :type includebody: bool

    """
    return web.Response(status=200)


async def content_search_content_by_tag_and_type(request: web.Request, locale, tag, type, currentpage=None, head=None, itemsperpage=None) -> web.Response:
    """content_search_content_by_tag_and_type

    Searches for Content Items that match the given Tag and Content Type.

    :param locale: 
    :type locale: str
    :param tag: 
    :type tag: str
    :param type: 
    :type type: str
    :param currentpage: Page number for the search results starting with page 1.
    :type currentpage: int
    :param head: Not used.
    :type head: bool
    :param itemsperpage: Not used.
    :type itemsperpage: int

    """
    return web.Response(status=200)


async def content_search_content_with_text(request: web.Request, locale, ctype=None, currentpage=None, head=None, searchtext=None, source=None, tag=None) -> web.Response:
    """content_search_content_with_text

    Gets content based on querystring information passed in. Provides basic search and text search capabilities.

    :param locale: 
    :type locale: str
    :param ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
    :type ctype: str
    :param currentpage: Page number for the search results, starting with page 1.
    :type currentpage: int
    :param head: Not used.
    :type head: bool
    :param searchtext: Word or phrase for the search.
    :type searchtext: str
    :param source: For analytics, hint at the part of the app that triggered the search. Optional.
    :type source: str
    :param tag: Tag used on the content to be searched.
    :type tag: str

    """
    return web.Response(status=200)


async def content_search_help_articles(request: web.Request, searchtext, size) -> web.Response:
    """content_search_help_articles

    Search for Help Articles.

    :param searchtext: 
    :type searchtext: str
    :param size: 
    :type size: str

    """
    return web.Response(status=200)
