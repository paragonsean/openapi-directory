from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_search_suggestions import AutocompleteSearchSuggestions
from openapi_server.models.error import Error
from openapi_server.models.top_searches import TopSearches
from openapi_server import util


async def autocomplete_suggestions_get(request: web.Request, query=None, locale=None) -> web.Response:
    """Get list of suggested terms and attributes similar to the search term

    Lists the suggested terms and attributes similar to the search term.

    :param query: Search term. It can contain any character.
    :type query: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str

    """
    return web.Response(status=200)


async def top_searches_get(request: web.Request, locale=None) -> web.Response:
    """Get list of the 10 most searched terms

    Lists the 10 most searched terms.

    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str

    """
    return web.Response(status=200)
