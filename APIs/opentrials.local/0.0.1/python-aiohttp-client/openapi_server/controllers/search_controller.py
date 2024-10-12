from typing import List, Dict
from aiohttp import web

from openapi_server.models.autocomplete_results import AutocompleteResults
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.fda_document_search_results import FDADocumentSearchResults
from openapi_server import util


async def autocomplete(request: web.Request, _in, q=None, page=None, per_page=None) -> web.Response:
    """autocomplete

    Autocomplete search feature for supported database entities (&#x60;location&#x60;). It has the same options as a regular &#x60;search&#x60; operation, with an extra **required** &#x60;in&#x60; parameter indicating the entity type to search.

    :param _in: The entity to search for
    :type _in: str
    :param q: The search query
    :type q: str
    :param page: The page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def search_fda_documents(request: web.Request, q=None, text=None, page=None, per_page=None) -> web.Response:
    """search_fda_documents

    Search the FDA documents

    :param q: The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
    :type q: str
    :param text: Search query on the documents file&#39;s text (follows the [ElasticSearch Simple Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-simple-query-string-query.html#_simple_query_string_syntax) syntax)
    :type text: str
    :param page: The page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
