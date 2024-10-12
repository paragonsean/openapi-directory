from typing import List, Dict
from aiohttp import web

from openapi_server.models.author import Author
from openapi_server.models.author_complete import AuthorComplete
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.private_authors_search import PrivateAuthorsSearch
from openapi_server import util


async def private_author_details(request: web.Request, author_id) -> web.Response:
    """Author details

    View author details

    :param author_id: Author unique identifier
    :type author_id: int

    """
    return web.Response(status=200)


async def private_authors_search(request: web.Request, body=None) -> web.Response:
    """Search Authors

    Search for authors

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = PrivateAuthorsSearch.from_dict(body)
    return web.Response(status=200)
