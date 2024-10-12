from typing import List, Dict
from aiohttp import web

from openapi_server.models.quote_response import QuoteResponse
from openapi_server import util


async def quote_delete(request: web.Request, id) -> web.Response:
    """quote_delete

    Delete a quote. The user needs to be the owner of the quote to be able to delete it. 

    :param id: Quote ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_get_0(request: web.Request, id=None) -> web.Response:
    """quote_get_0

    Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

    :param id: Quote ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_list_get(request: web.Request, start=None, limit=None) -> web.Response:
    """quote_list_get

    Get the list of quotes in your private collection.

    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param limit: Response is paged. This parameter controls how many is returned in the result.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_patch(request: web.Request, id, quote=None, author=None, language=None, tags=None) -> web.Response:
    """quote_patch

    Update a quote

    :param id: Quote ID
    :type id: str
    :param quote: Quote
    :type quote: str
    :param author: Quote Author
    :type author: str
    :param language: Language. If not supplied an auto detection mechanism will be used to detect a language.
    :type language: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_post(request: web.Request, quote, author=None, tags=None, language=None) -> web.Response:
    """quote_post

    Add a new quote to your private collection. Same as &#39;PUT&#39; but added since some clients don&#39;t handle PUT well.

    :param quote: Quote
    :type quote: str
    :param author: Quote Author
    :type author: str
    :param tags: Comma Separated tags
    :type tags: str
    :param language: Language. If not supplied an auto detection mechanism will be used to detect a language.
    :type language: str

    """
    return web.Response(status=200)


async def quote_put(request: web.Request, quote, author=None, tags=None, language=None) -> web.Response:
    """quote_put

    Add a new quote to your private collection.

    :param quote: Quote
    :type quote: str
    :param author: Quote Author
    :type author: str
    :param tags: Comma Separated tags
    :type tags: str
    :param language: Language. If not supplied an auto detection mechanism will be used to detect a language.
    :type language: str

    """
    return web.Response(status=200)


async def quote_tags_add_post(request: web.Request, id, tags) -> web.Response:
    """quote_tags_add_post

    Add a tag to a given Quote.

    :param id: Quote ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)


async def quote_tags_remove_post(request: web.Request, id, tags) -> web.Response:
    """quote_tags_remove_post

    Remove a tag from a given quote.

    :param id: Quote ID
    :type id: str
    :param tags: Comma Separated tags
    :type tags: str

    """
    return web.Response(status=200)
