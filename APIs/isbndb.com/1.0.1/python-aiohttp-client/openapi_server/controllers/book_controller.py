from typing import List, Dict
from aiohttp import web

from openapi_server.models.book import Book
from openapi_server import util


async def book_isbn_get(request: web.Request, isbn) -> web.Response:
    """Gets book details

    Returns the book details

    :param isbn: an ISBN 10 or ISBN 13 in the Books database
    :type isbn: str

    """
    return web.Response(status=200)


async def books_query_get(request: web.Request, query, page=None, author=None, page_size=None) -> web.Response:
    """Search books

    This returns a list of books that match the query

    :param query: A string to search for in the Book’s database
    :type query: str
    :param page: The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    :type page: str
    :param author: Filters the query results by author
    :type author: str
    :param page_size: How many items should be returned per page, maximum of 1,000
    :type page_size: str

    """
    return web.Response(status=200)
