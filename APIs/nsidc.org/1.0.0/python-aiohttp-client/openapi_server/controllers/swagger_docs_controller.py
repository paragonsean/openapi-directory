from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def facets(request: web.Request, search_terms=None, count=None, start_index=None, spatial=None, sort_keys=None, start_date=None, end_date=None, facet_filters=None, source=None) -> web.Response:
    """View the facet information corresponding to a search

    In the NSIDC Search and Arctic Data Explorer interfaces, this endpoint is used in conjunction with /OpenSearch whenever a user submits a new search. Consequently, it has the same parameters as /OpenSearch.

    :param search_terms: URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
    :type search_terms: str
    :param count: The number of search results per page desired by the client; OpenSearch 1.1
    :type count: int
    :param start_index: First search result desired by the search client; OpenSearch 1.1
    :type start_index: int
    :param spatial: 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter
    :type spatial: str
    :param sort_keys: Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
    :type sort_keys: str
    :param start_date: The start date in yyyy-mm-dd format
    :type start_date: str
    :param end_date: The end date in yyyy-mm-dd format
    :type end_date: str
    :param facet_filters: Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
    :type facet_filters: str
    :param source: Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    :type source: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def id(request: web.Request, q, source) -> web.Response:
    """Suggest search terms based on a partial query

    In NSIDC Search and the Arctic Data Explorer, this endpoint is queried whenever the user types into the search terms box, and the returned suggestions are displayed in a dropdown beneath the search terms box. The q parameter and returned JSON follow the specifications of the OpenSearch Suggestions 1.0 extension.

    :param q: Search terms typed into the interface (minimum two characters)
    :type q: str
    :param source: Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    :type source: str

    """
    return web.Response(status=200)


async def open_search(request: web.Request, search_terms=None, count=None, start_index=None, spatial=None, sort_keys=None, start_date=None, end_date=None, facet_filters=None, source=None) -> web.Response:
    """Search documents using the OpenSearch 1.1 Specification

    This endpoint uses parameters from the OpenSearch 1.1 specification, as well as parameters from the OpenSearch Geo (1.0) and SRU (1.0) extensions.

    :param search_terms: URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
    :type search_terms: str
    :param count: The number of search results per page desired by the client; OpenSearch 1.1
    :type count: int
    :param start_index: First search result desired by the search client; OpenSearch 1.1
    :type start_index: int
    :param spatial: 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter
    :type spatial: str
    :param sort_keys: Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
    :type sort_keys: str
    :param start_date: The start date in yyyy-mm-dd format
    :type start_date: str
    :param end_date: The end date in yyyy-mm-dd format
    :type end_date: str
    :param facet_filters: Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
    :type facet_filters: str
    :param source: Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    :type source: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def opensearch_description(request: web.Request, ) -> web.Response:
    """Describes the web interface of NSIDC&#39;s data search engine

    


    """
    return web.Response(status=200)
