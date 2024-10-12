from typing import List, Dict
from aiohttp import web

from openapi_server.models.quote_response import QuoteResponse
from openapi_server import util


async def quote_authors_popular_get(request: web.Request, language=None, detailed=None, start=None, limit=None) -> web.Response:
    """quote_authors_popular_get

    Gets a list of popular author names in the system.  

    :param language: Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil).
    :type language: str
    :param detailed: Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels.
    :type detailed: bool
    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param limit: Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_authors_search_get(request: web.Request, query=None, language=None, detailed=None, start=None, limit=None) -> web.Response:
    """quote_authors_search_get

    Gets a list of author names in the system.  

    :param query: Text string to search for in author names
    :type query: str
    :param language: Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil).
    :type language: str
    :param detailed: Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels.
    :type detailed: bool
    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param limit: Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_bookmark_toggle_get(request: web.Request, quote_id) -> web.Response:
    """quote_bookmark_toggle_get

    Toggle the user bookmark of the given Quote as a user of the API Key.

    :param quote_id: Quote ID
    :type quote_id: str

    """
    return web.Response(status=200)


async def quote_categories_popular_get(request: web.Request, start=None, limit=None) -> web.Response:
    """quote_categories_popular_get

    Gets a list of popular &#x60;Quote&#x60; Categories. 

    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param limit: Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_categories_search_get(request: web.Request, query=None, start=None, limit=None) -> web.Response:
    """quote_categories_search_get

    Gets a list of &#x60;Quote&#x60; Categories matching the query string. 

    :param query: Text string to search for in the categories
    :type query: str
    :param start: Response is paged. This parameter controls where response starts the listing at
    :type start: int
    :param limit: Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_get(request: web.Request, id=None) -> web.Response:
    """quote_get

    Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

    :param id: Quote ID
    :type id: str

    """
    return web.Response(status=200)


async def quote_like_toggle_get(request: web.Request, quote_id) -> web.Response:
    """quote_like_toggle_get

    Toggle the user like of the given Quote as a user of the API Key.

    :param quote_id: Quote ID
    :type quote_id: str

    """
    return web.Response(status=200)


async def quote_random_get(request: web.Request, language=None, limit=None) -> web.Response:
    """quote_random_get

    Gets a &#x60;Random Quote&#x60;. When you are in a hurry this is what you call to get a random famous quote.

    :param language: Language of the Quote. The language must be supported in our system.
    :type language: str
    :param limit: No of quotes to return. The max limit depends on the subscription level.
    :type limit: int

    """
    return web.Response(status=200)


async def quote_search_get(request: web.Request, category=None, author=None, minlength=None, maxlength=None, query=None, private=None, language=None, limit=None, sfw=None) -> web.Response:
    """quote_search_get

    Search for a &#x60;Quote&#x60; in They Said So platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the quote. 

    :param category: Quote Category
    :type category: str
    :param author: Quote Author
    :type author: str
    :param minlength: Quote minimum Length
    :type minlength: int
    :param maxlength: Quote maximum Length
    :type maxlength: int
    :param query: keyword to search for in the quote
    :type query: str
    :param private: Should search private collection? Default searches public collection.
    :type private: bool
    :param language: Language of the Quote. The language must be supported in our system.
    :type language: str
    :param limit: No of quotes to return. The max limit depends on the subscription level.
    :type limit: int
    :param sfw: Should search only SFW (Safe For Work) quotes?
    :type sfw: bool

    """
    return web.Response(status=200)
