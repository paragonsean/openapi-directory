from typing import List, Dict
from aiohttp import web

from openapi_server.models.package_search_result import PackageSearchResult
from openapi_server.models.search_result import SearchResult
from openapi_server import util


async def search(request: web.Request, query, match_mode=None) -> web.Response:
    """Searches through source code

    Performs a search through the full Debian Code Search corpus, blocking until all results are available (might take a few seconds depending on the search query).  Search results are ordered by their ranking (best results come first).

    :param query: The search query, for example &#x60;who knows...&#x60; (literal) or &#x60;who knows\\.\\.\\.&#x60; (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt
    :type query: str
    :param match_mode: Whether the query is to be interpreted as a literal (&#x60;literal&#x60;) instead of as an RE2 regular expression (&#x60;regexp&#x60;). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful.
    :type match_mode: str

    """
    return web.Response(status=200)


async def searchperpackage(request: web.Request, query, match_mode=None) -> web.Response:
    """Like /search, but aggregates per package

    The search results are currently sorted arbitrarily, but we intend to sort them by ranking eventually: https://github.com/Debian/dcs/blob/51338e934eb7ee18d00c5c18531c0790a83cb698/cmd/dcs-web/querymanager.go#L719

    :param query: The search query, for example &#x60;who knows...&#x60; (literal) or &#x60;who knows\\.\\.\\.&#x60; (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt
    :type query: str
    :param match_mode: Whether the query is to be interpreted as a literal (&#x60;literal&#x60;) instead of as an RE2 regular expression (&#x60;regexp&#x60;). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful.
    :type match_mode: str

    """
    return web.Response(status=200)
