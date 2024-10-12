from typing import List, Dict
from aiohttp import web

from openapi_server.models.author import Author
from openapi_server.models.author_query_results import AuthorQueryResults
from openapi_server import util


async def author_name_get(request: web.Request, name, page=None, page_size=None) -> web.Response:
    """Gets author details

    Returns the name and a list of books by the author.

    :param name: The name of an author in the Author&#39;s database
    :type name: str
    :param page: The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    :type page: str
    :param page_size: How many items should be returned per page, maximum of 1,000
    :type page_size: str

    """
    return web.Response(status=200)


async def authors_query_get(request: web.Request, query, page_size=None, page=None) -> web.Response:
    """Search authors

    This returns a list of authors whos name matches the given query

    :param query: A string to search for in the Author’s database
    :type query: str
    :param page_size: How many items should be returned per page, maximum of 1,000
    :type page_size: str
    :param page: The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    :type page: str

    """
    return web.Response(status=200)
